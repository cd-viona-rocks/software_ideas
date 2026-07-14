from .runnables.create_building import create_swimming_center

class App:

    def run(self):
        sw = create_swimming_center()


        print("App is running.")


if __name__ == "__main__":
    App().run()
