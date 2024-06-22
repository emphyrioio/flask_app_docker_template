from app import DevelopmentConfig, ProductionConfig, TestingConfig, create_app


def main() -> None:
    flask_app = create_app(DevelopmentConfig)
    flask_app.run()


if __name__ == "__main__":
    main()
