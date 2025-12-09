"""
Программа строит упрощённую натальную карту по дате, времени и координатам
места рождения. Требуемые зависимости: skyfield (и его efemerides DE421) и
zoneinfo (есть в Python 3.9+). Для работы без сети загрузите efemerides заранее:
`python - <<'PY'\nfrom skyfield.api import Loader\nLoader('~/.skyfield')('de421.bsp')\nPY`
"""

from __future__ import annotations

import argparse
import math
from datetime import datetime
from zoneinfo import ZoneInfo

from skyfield.api import Loader, Topos
from skyfield.units import Angle

ZODIAC_SIGNS = [
    "Овен",
    "Телец",
    "Близнецы",
    "Рак",
    "Лев",
    "Дева",
    "Весы",
    "Скорпион",
    "Стрелец",
    "Козерог",
    "Водолей",
    "Рыбы",
]

PLANETS = {
    "Солнце": "sun",
    "Луна": "moon",
    "Меркурий": "mercury",
    "Венера": "venus",
    "Марс": "mars",
    "Юпитер": "jupiter barycenter",
    "Сатурн": "saturn barycenter",
    "Уран": "uranus barycenter",
    "Нептун": "neptune barycenter",
    "Плутон": "pluto barycenter",
}


def normalize_angle(degrees_value: float) -> float:
    """Сводит угол к диапазону 0–360°."""
    return degrees_value % 360.0


def longitude_to_zodiac(longitude: Angle) -> tuple[str, float]:
    """Возвращает знак и градусы внутри знака для эклиптической долготы."""
    lon_deg = normalize_angle(longitude.degrees)
    sign_idx = int(lon_deg // 30)
    sign = ZODIAC_SIGNS[sign_idx]
    degrees_inside = lon_deg - sign_idx * 30
    return sign, degrees_inside


def ra_dec_to_ecliptic_longitude(ra: Angle, dec: Angle, epsilon_deg: float) -> float:
    """Преобразует прямое восхождение/склонение в эклиптическую долготу, °."""
    epsilon = math.radians(epsilon_deg)
    ra_rad = ra.radians
    dec_rad = dec.radians
    lon = math.atan2(
        math.sin(ra_rad) * math.cos(epsilon) + math.tan(dec_rad) * math.sin(epsilon),
        math.cos(ra_rad),
    )
    return normalize_angle(math.degrees(lon))


def true_obliquity_deg(t) -> float:
    """Истинный наклон эклиптики по формуле IAU, точнее фиксированной константы."""
    T = (t.tt - 2451545.0) / 36525.0  # юлианские столетия от J2000 по TT
    eps_sec = 84381.448 - 46.8150 * T - 0.00059 * (T**2) + 0.001813 * (T**3)
    return eps_sec / 3600.0


def compute_ascendant_and_mc(
    gast_hours: float, latitude_deg: float, longitude_deg: float, epsilon_deg: float
) -> tuple[float, float]:
    """
    Вычисляет долготы асцендента и MC (срединного неба).

    Формулы основаны на сферической астрономии (mean obliquity, локальное звёздное
    время = GAST + долгота).
    """
    theta = math.radians(gast_hours * 15.0 + longitude_deg)  # локальное звёздное время
    phi = math.radians(latitude_deg)
    epsilon = math.radians(epsilon_deg)

    asc_num = -math.cos(theta)
    asc_den = math.sin(epsilon) * math.tan(phi) + math.cos(epsilon) * math.sin(theta)
    asc = math.atan2(asc_num, asc_den)

    mc_num = math.sin(theta)
    mc_den = math.cos(theta) * math.cos(epsilon) - math.tan(phi) * math.sin(epsilon)
    mc = math.atan2(mc_num, mc_den)

    return normalize_angle(math.degrees(asc)), normalize_angle(math.degrees(mc))


def build_chart(birth_dt: datetime, latitude: float, longitude: float) -> list[tuple[str, str, float]]:
    """
    Строит упрощённую карту: планеты + асцендент + MC.

    birth_dt должен быть таймзон-aware (временная зона места рождения).
    """
    loader = Loader("~/.skyfield")
    ts = loader.timescale()
    eph = loader("de421.bsp")

    t = ts.from_datetime(birth_dt)
    earth = eph["earth"]
    earth_at = earth.at(t)
    observer = earth + Topos(latitude_degrees=latitude, longitude_degrees=longitude)  # noqa: F841

    epsilon = true_obliquity_deg(t)

    entries: list[tuple[str, str, float]] = []
    for name, key in PLANETS.items():
        astrometric = earth_at.observe(eph[key]).apparent()  # геоцентрическая позиция
        ra, dec, _ = astrometric.radec()
        lon_deg = ra_dec_to_ecliptic_longitude(ra, dec, epsilon)
        sign, deg_inside = longitude_to_zodiac(Angle(degrees=lon_deg))
        entries.append((name, sign, deg_inside))

    asc, mc = compute_ascendant_and_mc(t.gast, latitude, longitude, epsilon)
    asc_sign, asc_deg_inside = longitude_to_zodiac(Angle(degrees=asc))
    mc_sign, mc_deg_inside = longitude_to_zodiac(Angle(degrees=mc))
    entries.append(("Асцендент", asc_sign, asc_deg_inside))
    entries.append(("MC (Полдень)", mc_sign, mc_deg_inside))
    return entries


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Упрощённая натальная карта. " "На вход дата и время рождения (в местной зоне) и координаты места."
        )
    )
    parser.add_argument("--date", required=True, help="Дата рождения YYYY-MM-DD")
    parser.add_argument("--time", required=True, help="Время рождения HH:MM")
    parser.add_argument(
        "--tz",
        required=True,
        help="Часовой пояс в формате IANA, например Europe/Moscow",
    )
    parser.add_argument(
        "--lat",
        type=float,
        required=True,
        help="Широта места рождения, градусы (север +)",
    )
    parser.add_argument(
        "--lon",
        type=float,
        required=True,
        help="Долгота места рождения, градусы (восток +, запад -)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    birth_dt = datetime.strptime(f"{args.date} {args.time}", "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo(args.tz))

    chart = build_chart(birth_dt, latitude=args.lat, longitude=args.lon)

    print(f"Натальная карта для {birth_dt.isoformat()} " f"({args.lat:+.4f}, {args.lon:+.4f})")
    print("-" * 55)
    for name, sign, degrees_inside in chart:
        print(f"{name:12} → {sign:8} {degrees_inside:05.2f}°")


if __name__ == "__main__":
    main()
