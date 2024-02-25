import os
import unittest
from app.config import Config, DevelopmentConfig, ProductionConfig


class TestConfig(unittest.TestCase):
    def test_config_secret_key(self):
        config = Config()
        self.assertEqual(
            config.SECRET_KEY,
            os.environ.get("SECRET_KEY", "your_secret_key")
        )

    def test_config_database_uri(self):
        config = Config()
        self.assertEqual(
            config.SQLALCHEMY_DATABASE_URI,
            os.environ.get
            ("DATABASE_URL", "mysql://root:marwan@mysql-container/app")
        )

    def test_config_track_modifications(self):
        config = Config()
        self.assertFalse(config.SQLALCHEMY_TRACK_MODIFICATIONS)

    def test_development_config(self):
        config = DevelopmentConfig()
        self.assertTrue(config.DEBUG)
        self.assertEqual(
            config.SECRET_KEY,
            os.environ.get("SECRET_KEY", "your_secret_key")
        )
        self.assertEqual(
            config.SQLALCHEMY_DATABASE_URI,
            os.environ.get
            ("DATABASE_URL", "mysql://root:marwan@mysql-container/app")
        )
        self.assertFalse(config.SQLALCHEMY_TRACK_MODIFICATIONS)

    def test_production_config(self):
        config = ProductionConfig()
        self.assertFalse(config.DEBUG)
        self.assertEqual(
            config.SECRET_KEY,
            os.environ.get("SECRET_KEY", "your_secret_key")
        )
        self.assertEqual(
            config.SQLALCHEMY_DATABASE_URI,
            os.environ.get
            ("DATABASE_URL", "mysql://root:marwan@mysql-container/app")
        )
        self.assertFalse(config.SQLALCHEMY_TRACK_MODIFICATIONS)


if __name__ == '__main__':
    unittest.main()
