from app import DevelopmentConfig, ProductionConfig, TestingConfig, create_app


def main() -> None:
    app = create_app(DevelopmentConfig)
    app.run()


if __name__ == "__main__":
    main()
