from app import DevelopmentConfig, ProductionConfig, TestingConfig, create_app

app = create_app(DevelopmentConfig)
app.run()
