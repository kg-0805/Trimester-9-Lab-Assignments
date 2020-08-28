import java.io.*;
import java.util.*;


class mnt
{
    String macro_name;
    int mdt_index;

    mnt setupValues(String s, int mi) {
        mnt m = new mnt();
        m.macro_name = s;
        m.mdt_index = mi;
        return m;
    }
}


public class MacroPass1
{

    static void process(ArrayList<mnt> mn_table, ArrayList<String> md_table, ArrayList<String> ala_table)
    {
        try{
            File f = new File("input.txt");
            FileReader fr = new FileReader(f);
            BufferedReader br = new BufferedReader(fr);

            String line;
            int flag1 = 0,flag2=0;
            while((line = br.readLine()) != null)
            {
                String[] words = line.split(" ",0);
                if(flag1 == 1)
                {
                    if(flag2 == 1)
                    {
                        mnt curr = new mnt();
                        mn_table.add(curr.setupValues(words[0],md_table.size()));
                        flag2 = 0;
                        for(String s: words)
                        {
                            if(s.charAt(0) == '&')
                            {
                                ala_table.add(s);
                            }
                        }
                    }
                    md_table.add(line);
                }
                if(words[0].equals("MACRO"))
                {
                    flag1 = 1;
                    flag2 = 1;
                }
                if(flag1 ==0)
                {
                    System.out.println(line);
                }

                if(words[0] == "MEND")
                {
                    flag1 = 0;
                }
            }
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
        System.out.println("\nMNT TABLE \nIndex   Macro_Name  MDT_Index");
        System.out.println("\nMNT TABLE \nIndex   Macro_Name  MDT_Index");
        for(int i=0; i<mn_table.size(); i++) {
            mnt m = mn_table.get(i);
            System.out.println(i+1 +"        "+ m.macro_name +"         "+ m.mdt_index);
        }

        System.out.println("\nMDT Table\nIndex    Instructions");
        for(int i=0; i<md_table.size(); i++) {
            String m = md_table.get(i);
            System.out.println(i+1 +"       "+ m);
        }

        System.out.println("\nALA Table\nIndex  Dummy Arguments");
        for(int i=0; i<ala_table.size(); i++) {
            String m = ala_table.get(i);
            System.out.println(i+1 +"       "+ m);
        }
    }
    public static void main(String[] args)
    {
        ArrayList<mnt> mn_table = new ArrayList<mnt>();
        ArrayList<String> md_table = new ArrayList<String>();
        ArrayList<String> ala_table = new ArrayList<String>();

        process(mn_table,md_table,ala_table);
    }
}
