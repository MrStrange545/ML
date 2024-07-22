import java.util.*;
class test
{
    public static void main(String[] args)
    {
        Scanner scr = new Scanner(System.in);
        System.out.println("Enter a character:");
        double a = scr.nextDouble();
        double b = scr.nextDouble();
        double c = scr.nextDouble();
        double r = -b+Math.sqrt(b*b-4*a*c) /2*a;
        double s = -b-Math.sqrt(b*b-4*a*c) /2*a;
        System.out.println(r+" "+s); 
    }   
}