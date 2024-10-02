// creating a Record class with private attributes
class Record {
    private String recordID;
    private String customerID;
    private String loanType;
    private double interest;
    private double debt;
    private int years;

    // constructor to initialise the attributes
    public Record(String rID, String cID, String lType, double interest, double debt, int years) {
        this.recordID = rID;
        this.customerID = cID;
        this.loanType = lType;
        this.interest = interest;
        this.debt = debt;
        this.years = years;
    }

    // Getter Methods
    public String getRecordID() {
        return recordID;
    }

    public String getCustomerID() {
        return customerID;
    }

    public String getLoanType() {
        return loanType;
    }

    public double getInterestRate() {
        return interest;
    }

    public double getDebtAmount() {
        return debt;
    }

    public int getYears() {
        return years;
    }

    // Setter Methods
    public void setRecordID(String newRID) {
        recordID = newRID;
    }

    public void setCustomerID(String newCID) {
        customerID = newCID;
    }

    public void setLoanType(String newLType) {
        loanType = newLType;
    }

    public void setInterestRate(double newIRate) {
        interest = newIRate;
    }

    public void setDebtAmount(double newDebt) {
        debt = newDebt;
    }

    public void setYears(int newYrs) {
        years = newYrs;
    }

    // printing all the information in a formatted way
    public String PrintAll() {
        return String.format("%-12s %-15s %-12s %-12.2f %-15.3f %-15s", getRecordID(), getCustomerID(), getLoanType(), getInterestRate(), getDebtAmount(), getYears());
    }
}