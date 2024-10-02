import java.util.Scanner;
import java.util.regex.*;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

// XYZBank main class
public class XYZBank {
    // main
    public static void main(String[] args) {
        // new Scanner object initialised for processing user input
        Scanner input = new Scanner(System.in);

        // regular expressions to validate inputs -- Record ID & Customer ID
        String regex = "^[0-9]{6}$"; /* used for Record ID only when user decides to input */
        String regex2 = "^[A-Z]{3}[0-9]{3}$"; /* used for Customer ID only when user decided to input */

        // constant Strings to generate random values
        String upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; /* uppercase alphabet used for random generation for first 3 letters of Customer ID */
        String digits = "1234567890"; /* numbers from 0-9 used for random generation for Record ID and last 3 digits for Customer ID */

        // array of the types of loans and converting it to a list to validate user input -- Loan type
        String[] loanType = { "Auto", "Builder", "Mortgage", "Personal", "Other" };
        List<String> loan_Type = Arrays.asList(loanType);

        // compiling the regular expressions into Pattern object
        Pattern pattern = Pattern.compile(regex); /* for Record ID */
        Pattern pattern2 = Pattern.compile(regex2); /* for Customer ID */

        // initialising count to 0 to track number of records created
        int count = 0;

        // initialising number of record that the user would like to enter
        int recordNum = 0;
        // initialising boolean check value to verify user input is valid and loop if not
        boolean check = true;
        boolean choice = false;
        do {
            try {
                // user defined record number
                System.out.println("How many records would you like to create?");
                recordNum = input.nextInt();
                check = false;
            } catch (Exception e) {
                // catching and displaying error message if the input is invalid and letting them reinput
                System.out.println("Invalid input. Please enter an integer.");
                input.next();
                check = true;
            }
        } while (check != false);

        while (recordNum < 1) {
            // Exit the program if the user enters a number < 1 for number of records
            System.out.println("Enter valid number");
            recordNum = input.nextInt();
        }

        // array created of Record objects with the size entered by the user
        Record[] records = new Record[recordNum];

        // for loop for iterating through the max number of records initially set by the user
        for (int i = 0; i < recordNum; i++) {
            boolean oneMore = false;
            do {
                try {
                    // user enter if they would like another record to be created
                    System.out.println("Would you like to create a record: true or false?");
                    oneMore = input.nextBoolean();
                    check = false;
                } catch (Exception e) {
                    // error displayed if the input is not of boolean type
                    System.out.println("Type true for yes, false for no");
                    input.next();
                    check = true;
                }
            } while (check != false);

            // checking if they would like to add another record -- if yes:
            if (oneMore == true) {
                boolean valueType = false;
                do {
                    try {
                        // user input to pick between custom or default values
                        System.out.println("Would you like default values (true) or not (false)?");
                        valueType = input.nextBoolean();
                        check = false;
                    } catch (Exception e) {
                        // error displayed if input is not of boolean type
                        System.out.println("Invalid input. Please answer with 'true' or 'false'.");
                        input.next();
                        check = true;
                    }
                } while (check != false);

                // new Random object initialised to generate random values
                Random rand = new Random();

                // if they want a randomised default values
                if (valueType == true) {
                    // stringbuilder used to create string length of 6 using digits constant for record id
                    StringBuilder randRecordID = new StringBuilder();
                    // appending record id to string builder until it reaches desired length
                    for (int j = 0; j < 6; j++) {
                        randRecordID.append(digits.charAt(rand.nextInt(10)));
                    }
                    // if a repetition occurs then new record id is created
                    for (Record f : records) {
                        // overriding null error
                        if (f != null) {
                            do {
                                // re randomise if record id matches pre-existing one 
                                if (f.getRecordID().matches(randRecordID.toString())) {
                                    for (int j = 0; j < 6; j++) {
                                        randRecordID.append(digits.charAt(rand.nextInt(10)));
                                    }
                                    check = true;
                                } else {
                                    check = false;
                                }
                            } while (check != false);
                        }
                    }

                    // stringbuilder for customer id of length 6 using uppercase alphabet and digits constants 
                    StringBuilder randCustID = new StringBuilder();
                    for (int x = 0; x < 6; x++) {
                        // making sure first 3 values are uppercase alphabet
                        if (x < 3) {
                            randCustID.append(upperCase.charAt(rand.nextInt(26)));
                        } else {
                            // last 3 being digits
                            randCustID.append(digits.charAt(rand.nextInt(10)));
                        }
                    }

                    // picking random index in array of loantype to pick random loan type
                    int index = (int) (Math.random() * 5);
                    String randLoanType = loanType[index];

                    // using double for interest rate as it can be a decimal
                    double randInterest = 0;
                    // using double for the debt amount left to improve accuracy
                    double randDebt = 0;
                    // using int for years left
                    int randYears = 0;

                    // randomised  interest, debt and years based on the selected loan type to make it accurate to real life
                    if (randLoanType == "Auto") {
                        randInterest = rand.nextDouble(5, 20);

                        randDebt = rand.nextDouble(5000 / 1000, 50000 / 1000);

                        randYears = rand.nextInt(1, 5);
                    }
                    if (randLoanType == "Builder") {
                        randInterest = rand.nextDouble(1, 12);

                        randDebt = rand.nextDouble(5000 / 1000, 1000000 / 1000);

                        randYears = rand.nextInt(1, 3);
                    }
                    if (randLoanType == "Mortgage") {
                        randInterest = rand.nextDouble(3, 8);

                        randDebt = rand.nextDouble(100000 / 1000, 2000000 / 1000);

                        randYears = rand.nextInt(2, 40);
                    }
                    if (randLoanType == "Personal") {
                        randInterest = rand.nextDouble(10, 30);

                        randDebt = rand.nextDouble(1000 / 1000, 50000 / 1000);

                        randYears = rand.nextInt(1, 10);
                    }
                    if (randLoanType == "Other") {
                        randInterest = rand.nextDouble(0, 200);

                        randDebt = rand.nextDouble(1 / 1000, 500000 / 1000);

                        randYears = rand.nextInt(1, 40);
                    }
                    // adding the attributes to the Record array
                    records[i] = new Record(randRecordID.toString(), randCustID.toString(), randLoanType, randInterest, randDebt, randYears);
                    // adding 1 to count to keep track of registered records
                    count += 1;
                } else {
                    String recordID = "";
                    // used to check for the format of the inputs
                    Matcher matcher;
                    do {
                        // record id attribute input
                        System.out.println("Enter your 6 digit record id");
                        recordID = input.next();

                        // checking pre-existing records to make sure record id doesn't match
                        for (Record f : records) {
                            // overriding null error
                            if (f != null) {
                                do {
                                    // reinput if record id matches pre-existing one 
                                    if (f.getRecordID().matches(recordID)) {
                                        System.err.println("Record ID already exists, try again");
                                        recordID = input.next();
                                        check = true;
                                    } else {
                                        check = false;
                                    }
                                } while (check != false);
                            }
                        }
                        // making sure the record id matches the pattern of "XXXXXX" X = numbers from 0-9
                        matcher = pattern.matcher(recordID);

                    } while (!matcher.matches());

                    String custID = "";
                    Matcher matcher2;
                    do {
                        // customer id attribute input
                        System.out.println("Enter customer id in the format 'ABC123'");
                        custID = input.next();

                        // making sure the customer id matches the pattern of "AAAXXX" A = capital alphabet, X = numbers from 0-9
                        matcher2 = pattern2.matcher(custID);
                    } while (!matcher2.matches());

                    String loan_type = "";
                    do {
                        // loan type attribute input
                        System.out.println("Enter loan type: Auto, Builder, Mortgage, Personal, Other");
                        loan_type = input.next();

                    } while (!loan_Type.contains(loan_type)); /* checking until the input is valid using the ArrayList */

                    double intRate = 0;
                    do {
                        try {
                            // interest rate attribute input
                            System.out.println("Enter interest rate on debt");
                            intRate = input.nextDouble();
                            if (intRate < 0) {
                                // making sure interest rate isn't below 0 since banks would most likely want to make some profit on lending
                                do {
                                    System.out.println("Enter a positive interest rate");
                                    intRate = input.nextDouble();
                                } while (intRate <= 0);
                            }
                            check = false;
                        } catch (Exception e) {
                            // catching exception if non-numeric data is entered
                            System.out.println("Enter valid interest rate");
                            input.next();
                            check = true;
                        }
                    } while (check != false);

                    double leftAmount = 0;
                    do {
                        try {
                            // amount left attribute input
                            System.out.println("Enter amount left to pay in thousands");
                            leftAmount = input.nextInt();
                            if (leftAmount < 0) {
                                // making sure the amount left isn't below 0
                                do {
                                    System.out.println("Enter amount > 0");
                                    leftAmount = input.nextDouble();
                                } while (leftAmount <= 0);
                            }
                            check = false;
                        } catch (Exception e) {
                            // catching exception for non-numeric input
                            System.out.println("Enter valid amount left to pay in thousands");
                            input.next();
                            check = true;
                        }
                    } while (check != false);

                    int timeLeft = 0;
                    do {
                        try {
                            // years left attribute input
                            System.out.println("Enter amount of years left to pay off the loan");
                            timeLeft = input.nextInt();
                            if (timeLeft < 0) {
                                do {
                                    // making sure the number of years isn't below 0
                                    System.out.println("Enter years > 0");
                                    timeLeft = input.nextInt();
                                } while (timeLeft <= 0);
                            }
                            check = false;
                        } catch (Exception e) {
                            // catching error for non-integer inputs
                            System.out.println("Enter valid number of years left");
                            input.next();
                            check = true;
                        }
                    } while (check != false);

                    // adding the attributes into the Record array
                    records[i] = new Record(recordID, custID, loan_type, intRate, leftAmount, timeLeft);
                    // increasing count by 1 to keep track of registered records
                    count += 1;
                }
            }
            // when user doesn't want to input new record
            else{
                do{
                    try{
                        // give user choice to exit creating records
                        System.out.println("Would you like to exit making new records?");
                        choice = input.nextBoolean();
                        if (choice == true){
                            check = false;
                            break;
                        }
                        // if user inputs false, decrease i by 1 to let them input again
                        else{
                            i = i - 1;
                            check = false;
                            continue;
                        }
                    }
                    // checking user inputs a boolean value
                    catch(Exception e){
                        System.out.println("Enter either true or false");
                        input.next();
                        check = true;
                    }
                }while(check != false);
            }
            // breaking the for loop if user chooses to exit making new records
            if(choice == true){
                break;
            }
        }
        // printing maximum number of records
        System.out.println("\nMaximum number of Records: " + recordNum);
        // printing the registered number of records
        System.out.println("Registered Records: " + count + "\n");
        // printing the record headings in a formatted way
        System.out.printf("%-12s %-15s %-12s %-12s %-15s %-15s\n", "RecordID", "CustomerID", "LoanType", "IntRate(%)", "AmountLeft(k)", "TimeLeft(Yrs)");
        // loop through all record objects and print their attributes in a formatted way
        for (int p = 0; p < recordNum; p++) {
            try {
                System.out.println(records[p].PrintAll());
            } catch (Exception e) /* catching null exception */ {
                continue;
            }
        }
        // closing the Scanner
        input.close();
    }
}