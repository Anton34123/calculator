import loop
import classes

def main():
    c = classes.Calculate()
    print(c.get_result())

if __name__ == "__main__":
    loop.loop_(main)
