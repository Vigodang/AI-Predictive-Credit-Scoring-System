"""
Database Configuration
Cấu hình kết nối MySQL cho ứng dụng Credit Risk Scoring
"""
import os
from typing import Dict


class DatabaseConfig:
    """
    Lớp cấu hình database MySQL
    """
    
    def __init__(
        self,
        host: str = None,
        port: int = None,
        user: str = None,
        password: str = None,
        database: str = None
    ):
        """
        Khởi tạo cấu hình database
        
        Args:
            host: MySQL host address
            port: MySQL port (mặc định 3306)
            user: MySQL username
            password: MySQL password
            database: Tên database
        """
        self.host = host or os.getenv('CREDIT_DB_HOST', 'localhost')
        self.port = port or int(os.getenv('CREDIT_DB_PORT', '3306'))
        self.user = user or os.getenv('CREDIT_DB_USER', 'root')
        self.password = password if password is not None else os.getenv('CREDIT_DB_PASSWORD', '')
        self.database = database or os.getenv('CREDIT_DB_NAME', 'credit_risk_db')
    
    def to_dict(self) -> Dict[str, any]:
        """
        Chuyển cấu hình thành dictionary để dùng cho mysql.connector
        
        Returns:
            Dict chứa các thông số kết nối
        """
        return {
            'host': self.host,
            'port': self.port,
            'user': self.user,
            'password': self.password,
            'database': self.database,
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_unicode_ci'
        }
    
    @classmethod
    def default(cls) -> 'DatabaseConfig':
        """
        Trả về cấu hình mặc định
        
        Returns:
            Instance DatabaseConfig với các giá trị mặc định
        """
        return cls()
