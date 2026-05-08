package LEARNING.JavaTutorial;

public class stringMethods {

    String name;

    boolean isJoshua    = name.equals("Joshua");                // returns a boolean true or false depending on if the value is the same
    boolean isJoshua0   = name.equalsIgnoreCase("joshua"); // doesn't care about the case, upper or lower
        int result      = name.length();                                 // result is now an int equal to the # of characters, including the spaces in name
       char firstLetter = name.charAt(0);                          // 0 is the first letter in the in the String name. Returns whatever the char at that specific point is
        int whereIsJ    = name.indexOf("J");                         // This returns the position of the specific letter in the String, opposite of charAt
    boolean isEmpty     = name.isEmpty();                                // This return a boolean true or false if the value is empty or ""
     String upperCaseNm = name.toUpperCase();                            // returns the fully uppercased version of the string
     String lowerCaseNm = name.toLowerCase();                            // returns the fully lowercased version of the string
     String wthotWhtSpc = name.trim();                                   // Like the strip() method in python, will remove whitespace.
     String replacechar = name.replace('a', 'o');       // This will replace ALL the chars a to o's, remember to put it in single quotes because its a char.
    public static void main(String[] args) {
        
        stringMethods infoAbName = new stringMethods();

        System.out.println(
            infoAbName.isJoshua    + "\n"+
            infoAbName.isJoshua0   + "\n"+
            infoAbName.result      + "\n"+
            infoAbName.firstLetter + "\n"+
            infoAbName.whereIsJ    + "\n"+
            infoAbName.isEmpty     + "\n"+
            infoAbName.upperCaseNm + "\n"+
            infoAbName.lowerCaseNm + "\n"+
            infoAbName.wthotWhtSpc + "\n"+
            infoAbName.replacechar + "\n"
        );
        
    }
}
