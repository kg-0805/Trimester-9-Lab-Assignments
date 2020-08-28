import java.io.*;
import java.util.*;
import java.lang.*;


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

class param
{
    String param_name;
    String assigned_param;

    param initialize(String pn,String apn)
    {
        param p = new param();
        p.param_name = pn;
        p.assigned_param = apn;
        return p;
    }
}


public class MacroPass2
{

    static void macropass1(ArrayList<mnt> mn_table, ArrayList<String> md_table, ArrayList<String> ala_table)
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

                if(words[0].equals("MEND"))
                {
                    flag1 = 0;
                }
            }

            System.out.println("\nMNT TABLE \nIndex   Macro_Name  MDT_Index");
            for(int i=0; i<mn_table.size(); i++)
            {
                mnt m = mn_table.get(i);
                System.out.println(i+1 +"        "+ m.macro_name +"         "+ m.mdt_index);
            }

            System.out.println("\nMDT Table\nIndex    Instructions");
            for(int i=0; i<md_table.size(); i++) {
                String m = md_table.get(i);
                System.out.println(i+1 +"       "+ m);
            }

            System.out.println("\nALA Table\nIndex  Dummy Arguments");
            for(int i=0; i<ala_table.size(); i++)
            {
                String m = ala_table.get(i);
                System.out.println(i+1 +"       "+ m);
            }

        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
    }

    static ArrayList paramCheck(ArrayList<String> ala_table, String line)
    {
        ArrayList<param> param_table = new ArrayList<param>();
        String[] words = line.split(" ",0);
        for(int i =1; i<words.length; i++)
        {
            param p = new param();
            p.param_name = ala_table.get(i-1);
            p.assigned_param = words[i];
            param_table.add(p);
        }
        return param_table;
    }

    static String paramFill(ArrayList<param> p_table, String line)
    {
        String[] words = line.split(" ",0);
        for(int i=1;i<words.length;i++)
        {
            String token = words[i];
            for(int j=0;j<p_table.size();j++)
            {
                param p = p_table.get(j);
                if(token.equals(p.param_name))
                {
                    words[i] = p.assigned_param;
                }
            }
        }
        String new_text = "";
        for(int i=0;i<words.length;i++)
        {
            new_text += words[i];
            new_text += " ";
        }

        return new_text;
    }

    static void macropass2(ArrayList<mnt> mn_table, ArrayList<String> md_table,ArrayList<String> ala_table)
    {
        try
        {
            File f = new File("input.txt");
            FileReader fr = new FileReader(f);
            BufferedReader br = new BufferedReader(fr);
            String line;
            int flag1=0,flag2=0;

            ArrayList<param> p_table = new ArrayList<param>();
            System.out.println("\nExpanded Code:\n");

            while((line = br.readLine()) != null)
            {
                String[] words = line.split(" ",0);
                if(words[0].equals("MACRO"))
                {
                    flag1 = 1;
                }
                if(flag1 != 1)
                {
                    int found = 0;
                    for(int i=0; i<mn_table.size(); i++)
                    {
                        mnt m = mn_table.get(i);
                        if(words[0].equals(m.macro_name))
                        {
                            found = 1;
                            p_table = paramCheck(ala_table,line);
                            int mdi = m.mdt_index;
                            mdi++;

                            String mtext = md_table.get(mdi);
                            while(!mtext.equals("MEND"))
                            {
                                mtext = paramFill(p_table,mtext);
                                System.out.println(mtext);
                                mtext = md_table.get(mdi);
                                mdi++;
                            }
                        }
                    }
                    if(found == 0)
                    {
                        System.out.println(line);
                    }
                    if (found == 1)
                    {
                        found = 0;
                    }
                }
                if(words[0].equals("MEND"))
                {
                    flag1 = 0;
                }
            }
            System.out.println("\nMNT TABLE \nIndex   Macro_Name  MDT_Index");
            for(int i=0; i<mn_table.size(); i++)
            {
                mnt m = mn_table.get(i);
                System.out.println(i+1 +"        "+ m.macro_name +"         "+ m.mdt_index);
            }

            System.out.println("\nMDT Table\nIndex    Instructions");
            for(int i=0; i<md_table.size(); i++) {
                String m = md_table.get(i);
                System.out.println(i+1 +"       "+ m);
            }

            System.out.println("\nALA Table\nIndex  Dummy Arguments");
            for(int i=0; i<ala_table.size(); i++)
            {
                String m = ala_table.get(i);
                System.out.println(i+1 +"       "+ m);
            }

            System.out.println("\nParameter Table \nIndex   Param_Name  ASS_Name");
            for(int i=0; i<p_table.size(); i++) {
                param p = p_table.get(i);
                System.out.println(i+1 +"        "+ p.param_name +"         "+ p.assigned_param);
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
    public static void main(String[] args)
    {
        ArrayList<mnt> mn_table = new ArrayList<mnt>();
        ArrayList<String> md_table = new ArrayList<String>();
        ArrayList<String> ala_table = new ArrayList<String>();

        macropass1(mn_table,md_table,ala_table);
        macropass2(mn_table,md_table,ala_table);
    }
}