def generate(n):
    result = []

    def generate_(left, right, stack, accum):
        if not left and not right:
            result.append(accum)
            return
        if left > 0:
            generate_(left - 1, right, stack + 1, accum + "(")
        if right > 0 and stack > 0:
            generate_(left, right - 1, stack - 1, accum + ")")

    generate_(n, n, 0, "")
    return result


if __name__ == "__main__":
    n = int(input())
    print(generate(n))
