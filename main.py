from src.kombat import Kombat


def run():
    kombat = Kombat()
    kombat.start()


if __name__ == "__main__":
    while True:
        try:
            run()
        except KeyboardInterrupt:
            print("\n👾 game over 👾")
            break
