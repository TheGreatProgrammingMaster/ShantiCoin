import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QGridLayout, QGroupBox, QPlainTextEdit
from PyQt6.QtGui import QFont
from blockchain import Blockchain

class BlockchainWallet(QWidget):
    def __init__(self):
        super().__init__()

        self.blockchain = Blockchain()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Blockchain Wallet')
        self.setGeometry(100, 100, 1000, 700)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Header
        header_frame = QFrame()
        header_layout = QHBoxLayout()
        balance_label = QLabel('Balance: $123.45')
        balance_label.setFont(QFont('Arial', 24))
        address_label = QLabel('Address: 4...abc')
        address_label.setFont(QFont('Arial', 18))
        header_layout.addWidget(balance_label)
        header_layout.addStretch()
        header_layout.addWidget(address_label)
        header_frame.setLayout(header_layout)
        main_layout.addWidget(header_frame)

        # Navigation
        nav_frame = QFrame()
        nav_layout = QHBoxLayout()
        dashboard_button = QPushButton('Dashboard')
        dashboard_button.setFixedWidth(150)
        send_button = QPushButton('Send')
        send_button.setFixedWidth(150)
        receive_button = QPushButton('Receive')
        receive_button.setFixedWidth(150)
        transactions_button = QPushButton('Transactions')
        transactions_button.setFixedWidth(150)
        nav_layout.addWidget(dashboard_button)
        nav_layout.addWidget(send_button)
        nav_layout.addWidget(receive_button)
        nav_layout.addWidget(transactions_button)
        nav_frame.setLayout(nav_layout)
        main_layout.addWidget(nav_frame)

        # Content
        content_frame = QGroupBox('Blockchain Overview')
        content_layout = QGridLayout()
        blockchain_height_label = QLabel('Blockchain Height: 123456')
        connections_label = QLabel('Connections: 10')
        difficulty_label = QLabel('Difficulty: 123.45')
        content_layout.addWidget(blockchain_height_label, 0, 0)
        content_layout.addWidget(connections_label, 1, 0)
        content_layout.addWidget(difficulty_label, 2, 0)
        content_frame.setLayout(content_layout)
        main_layout.addWidget(content_frame)

        # Transaction Log
        log_frame = QGroupBox('Transaction Log')
        log_layout = QVBoxLayout()
        self.log_text = QPlainTextEdit()
        log_layout.addWidget(self.log_text)
        log_frame.setLayout(log_layout)
        main_layout.addWidget(log_frame)

        # Mine Block Button
        mine_button = QPushButton('Mine Block')
        mine_button.clicked.connect(self.mine_block)
        main_layout.addWidget(mine_button)

        self.setLayout(main_layout)

    def mine_block(self):
        self.blockchain.mine_block_scrypt()
        self.log_text.appendPlainText(f'Block mined successfully! Height: {len(self.blockchain.chain)}')


def main():
    app = QApplication(sys.argv)
    wallet = BlockchainWallet()
    wallet.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()