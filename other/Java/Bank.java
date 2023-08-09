import java.util.ArrayList;

class Bank {
    private String name;
    protected String routing;
    private ArrayList<Account> accounts;

    public Bank(String name) {
        this.name = name;
        this.accounts = new ArrayList<>();
    }

    public void addAccount(Account acc) {
        accounts.add(acc);
    }

    public Account getAccount(int accountNumber) {
        for (Account account : accounts) {
            if (account.getAccountNumber() == accountNumber) {
                return account;
            }
        }
        return null;
    }
}

class Account {
    private int accountNumber;
    private String accountName;
    private double balance;
    private CreditCard credit;
    private DebitCard debit;

    public Account(int accountNumber, String accountName, double balance) {
        this.accountNumber = accountNumber;
        this.accountName = accountName;
        this.balance = balance;
        credit = new CreditCard("1234567890123456", accountName);
        debit = new DebitCard("6543210987654321", accountName);
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public String getAccountName() {
        return accountName;
    }

    // these can change into using the debit/credit balance/methods now
    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        } else {
            System.out.println("not a valid deposit amount.");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        } else {
            System.out.println("Invalid amount or not enough funds");
        }
    }
}

abstract class Card {
    protected String cardNumber;
    protected String name;
    protected double balance;
    protected int code;

    public Card(String cardNumber, String name) {
        this.cardNumber = cardNumber;
        this.name = name;
        this.balance = 0.00;
        this.code = 0000;
    }

    public String getName() {
        return name;
    }

    public String getCardNumber() {
        return cardNumber;
    }

    public double getBalance() {
        return balance;
    }

    public int getCode() {
        return code;
    }

    public void setCardNumber(String number) {
        // do stuff here to set number
    }

    public void setCode(int code) {
        // do stuff here to set code
    }
}

class CreditCard extends Card {
    private double limit;
    private double charges;

    public CreditCard(String cardNumber, String name) {
        super(cardNumber, name);
        limit = 2000.00;
    }

    public double getLimit() {
        return limit;
    }

    public double remainingLimit() {
        return limit - charges;
    }

    public void charge(double amount) {
        if (limit - charges > amount) {
            charges += amount;
        } else {
            System.out.print("Invalid amount or too little limit");
        }
    }

    public void payBalance(double amount) {
        if (amount > 0 && amount <= charges) {
            charges -= amount;
        } else {
            System.out.println("Invalid amount or paying more than owed");
        }
    }

}

class DebitCard extends Card {
    // Similar to CreditCard
    public double balance;

    public DebitCard(String cardNumber, String name) {
        super(cardNumber, name);
        balance = 0.00;
    }
}