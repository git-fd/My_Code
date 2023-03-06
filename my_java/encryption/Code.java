package my_java.encryption;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.Random;
import java.io.FileReader;

public class Code {
    private String path;

    public Code(String path) {
        this.path = path; 
    }

    public int encrypt() throws IOException {

        File infile = new File(this.path);
        int pos = this.path.lastIndexOf(".");

        String newpath = this.path.substring(0, pos) + ".cod";
        String suffix = this.path.substring(pos);

        if (infile.exists()) {

            if (this.path.substring(pos).equals(".cod")) {
                System.out.println("文件已加密");
                return 1;
            }

            File outfile = new File(newpath);

            outfile.createNewFile();

            FileReader reader = new FileReader(infile);
            FileWriter writer = new FileWriter(outfile);

            int data, index = 0;
            String str = "!@#$%^&*()_+-=,./;'[]<>?:{}\"1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
            Random r = new Random();

            while ((data = reader.read()) != -1) {
                char c = (char) data;
                for (int i = 0; i < str.length(); ++i) {
                    if (i == index) {
                        writer.append(c);
                    } else {
                        writer.append(str.charAt(r.nextInt(0, str.length())));
                    }
                }
                writer.append('\n');
                index++;
                if (index == str.length())
                    index = 0;
            }

            for (int i = 0; i < str.length() - suffix.length(); ++i) {
                writer.append(str.charAt(r.nextInt(0, str.length())));
            }
            writer.append(suffix);

            reader.close();
            writer.close();

            infile.delete();

        } else {
            System.out.println("文件不存在");
            return -1;
        }

        System.out.println("加密成功");
        return 0;
    }

    public int decode() throws IOException {

        File infile = new File(this.path);

        int pos = this.path.lastIndexOf(".");

        String newpath = this.path.substring(0, this.path.length() - 4);

        if (infile.exists()) {

            if (!this.path.substring(pos).equals(".cod")) {
                System.out.println("文件未加密");
                return 1;
            }

            File outfile = new File(newpath);

            outfile.createNewFile();

            FileReader reader = new FileReader(infile);
            FileWriter writer = new FileWriter(outfile);
            int data, index = 0, cur = 0;
            String str = "!@#$%^&*()_+-=,./;'[]<>?:{}\"1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
            String suffix = getFileSuffix(this.path);

            while ((data = reader.read()) != -1) {
                char c = (char) data;
                if (cur == index)
                    writer.append(c);
                if (cur == str.length()) {
                    cur = -1;
                    index++;
                    if (index == str.length()) {
                        index = 0;
                    }
                }
                cur++;
            }

            reader.close();
            writer.close();
            
            outfile.renameTo(new File(outfile + suffix));
            infile.delete();

        } else {
            System.out.println("文件不存在");
            return -1;
        }

        System.out.println("解密成功");
        return 0;
    }

    public String getFileSuffix(String path) throws IOException {

        RandomAccessFile f = new RandomAccessFile(path, "rw");
        StringBuffer sb = new StringBuffer();
        boolean st = true;
        long length = f.length() - 1;
        f.seek(length);
        int data = f.read();
        while(((char)data) != '\n') {
            if (st) {
                sb.append((char)data);
                st = (char)data != '.';
            }
            length--;
            f.seek(length);
            data = f.read();
        }
        
        f.setLength(length + 1);
        f.close();

        return sb.reverse().toString();
    }
}