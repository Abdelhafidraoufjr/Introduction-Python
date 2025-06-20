
class BankAccount:

    # ───────────── Construction ─────────────
    def __init__(self, balance: int = 0, *, username: str | None = None,
                 password: str | None = None) -> None:
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance: int = balance
        self.username: str | None = username
        self.password: str | None = password
        self.authenticated: bool = False    # Part III

    # ───────────── Authentication (Part III) ─────────────
    def authenticate(self, username: str, password: str) -> None:

        if self.username is None or self.password is None:
            raise RuntimeError("Account has no credentials set.")
        if username == self.username and password == self.password:
            self.authenticated = True
        else:
            raise PermissionError("Bad credentials.")

    # ───────────── Operations ─────────────
    def deposit(self, amount: int) -> None:
        self._ensure_authenticated()
        self._validate_positive(amount)
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self._ensure_authenticated()
        self._validate_positive(amount)
        self.balance -= amount

    # ───────────── Helpers ─────────────
    def _ensure_authenticated(self) -> None:
        if not self.authenticated:
            raise PermissionError("Operation requires authentication.")

    @staticmethod
    def _validate_positive(value: int) -> None:
        if value <= 0:
            raise ValueError("Amount must be a positive integer.")

    # ───────────── Convenience ─────────────
    def __repr__(self) -> str:
        return f"<BankAccount balance={self.balance}>"

class MinimumBalanceAccount(BankAccount):

    def __init__(self, balance: int = 0, *, minimum_balance: int = 0,
                 username: str | None = None, password: str | None = None) -> None:
        super().__init__(balance, username=username, password=password)
        if minimum_balance < 0:
            raise ValueError("Minimum balance cannot be negative.")
        self.minimum_balance = minimum_balance

    def withdraw(self, amount: int) -> None:        # override
        self._ensure_authenticated()
        self._validate_positive(amount)
        if self.balance - amount < self.minimum_balance:
            raise ValueError("Withdrawal would breach minimum balance.")
        self.balance -= amount

    def __repr__(self) -> str:
        return (f"<MinimumBalanceAccount balance={self.balance} "
                f"min={self.minimum_balance}>")

class ATM:


    def __init__(self, account_list, try_limit: int = 2) -> None:
        # Validate accounts
        if not all(isinstance(a, BankAccount) for a in account_list):
            raise TypeError("account_list must contain BankAccount instances.")
        self.accounts = account_list

        # Validate try_limit
        if try_limit <= 0:
            raise ValueError("try_limit must be positive.")
        self.try_limit = try_limit
        self.current_tries = 0

        self.show_main_menu()

    def show_main_menu(self) -> None:
        while True:
            print("\n=== MAIN MENU ===")
            print("1) Log in")
            print("2) Exit")
            choice = input("Select option: ").strip()
            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Good‑bye.")
                break
            else:
                print("Unknown choice, try again.")

    def log_in(self, username: str, password: str) -> None:
        for acc in self.accounts:
            try:
                acc.authenticate(username, password)
                print(f"Welcome, {username}!")
                self.current_tries = 0  # reset counter
                self.show_account_menu(acc)
                return
            except PermissionError:
                pass   

        self.current_tries += 1
        remaining = self.try_limit - self.current_tries
        if remaining <= 0:
            print("Max login attempts reached. Shutting down.")
            raise SystemExit
        print(f"Login failed. Attempts remaining: {remaining}")

    def show_account_menu(self, account: BankAccount) -> None:
        while True:
            print(f"\n=== ACCOUNT MENU (balance {account.balance}) ===")
            print("1) Deposit")
            print("2) Withdraw")
            print("3) Exit to main menu")
            choice = input("Select option: ").strip()
            if choice == "1":
                amount = int(input("Amount to deposit: "))
                try:
                    account.deposit(amount)
                    print(f"Deposited. New balance: {account.balance}")
                except Exception as err:
                    print("Error:", err)
            elif choice == "2":
                amount = int(input("Amount to withdraw: "))
                try:
                    account.withdraw(amount)
                    print(f"Withdrawn. New balance: {account.balance}")
                except Exception as err:
                    print("Error:", err)
            elif choice == "3":
                print("Logging out.")
                account.authenticated = False
                break
            else:
                print("Unknown choice, try again.")


if __name__ == "__main__":
    acct1 = BankAccount(500, username="alice", password="wonder")
    acct2 = MinimumBalanceAccount(800, minimum_balance=200,
                                  username="bob", password="builder")


    ATM([acct1, acct2], try_limit=3)
