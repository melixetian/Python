from dataclasses import dataclass, field


@dataclass
class Category:
    id: str
    parent_id: str | None = None


@dataclass
class Hierarchy:
    id: str
    children: list["Hierarchy"] = field(default_factory=list)


def build_hierarchy(categories: list[Category]) -> list[Hierarchy]:
    nodes = {category.id: Hierarchy(category.id) for category in categories}
    roots: list[Hierarchy] = []

    for category in categories:
        node = nodes[category.id]

        if category.parent_id is None:
            roots.append(node)
        else:
            parent = nodes[category.parent_id]
            parent.children.append(node)

    return roots
