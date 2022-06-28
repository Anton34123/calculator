import loop


def main():
    m_e = input("Enter mathematical expression: ")
    vc = "1234567890+-*/()."  # valid characters
    acc = True

    for char in m_e:
        if char not in vc:
            acc = False

    if acc:
        print(eval(m_e))
    else:
        print("Non corrected enter")


if __name__ == "__main__":
    loop.loop_(main)
