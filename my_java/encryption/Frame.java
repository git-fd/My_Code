package my_java.encryption;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.io.File;
import java.io.IOException;

public class Frame extends JFrame implements ActionListener {

    private JFileChooser jfc = new JFileChooser("D:\\");
    private JButton[] jb = { new JButton("选择文件"), new JButton("加密"), new JButton("解密") };
    private JPanel jphome = new JPanel();
    private JPanel jpjfc = new JPanel();
    private JTextField jf = new JTextField(25);

    public Frame() {
        this.setTitle("文件加密");
        this.setBounds(480, 200, 600, 380);
        this.setDefaultCloseOperation(3);
        jphome.setLayout(null);

        Frame outer = this;

        jf.setBounds(100, 80, 250, 30);
        jb[0].setBounds(360, 80, 100, 30);
        jb[1].setBounds(150, 200, 100, 30);
        jb[2].setBounds(310, 200, 100, 30);

        jpjfc.add(jfc);

        jb[0].addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                outer.jfc.rescanCurrentDirectory();
                outer.jphome.setVisible(false);
                outer.setContentPane(jpjfc);
                outer.jpjfc.setVisible(true);
            }
        });

        jb[1].addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!jf.getText().equals("")) {
                    try {
                        int status = new Code(jf.getText()).encrypt();
                        if (status == 0) {
                            JOptionPane.showMessageDialog(null, "加密成功");
                            outer.jf.setText("");
                        } else if (status == 1) {
                            JOptionPane.showMessageDialog(null, "文件已加密");
                        } else if (status == -1) {
                            JOptionPane.showMessageDialog(null, "文件不存在");
                        }
                    } catch (IOException x) {
                        System.out.println("Error!!!");
                    }
                } else {
                    System.out.println("请选择文件");
                    JOptionPane.showMessageDialog(null, "请选择文件");
                }
            }
        });

        jb[2].addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!jf.getText().equals("")) {
                    try {
                        int status = new Code(jf.getText()).decode();
                        if (status == 0) {
                            JOptionPane.showMessageDialog(null, "解密成功");
                            outer.jf.setText("");
                        } else if (status == 1) {
                            JOptionPane.showMessageDialog(null, "文件未加密");
                        } else if (status == -1) {
                            JOptionPane.showMessageDialog(null, "文件不存在");
                        }
                    } catch (IOException x) {
                        System.out.println("Error!!!");
                    }
                } else {
                    System.out.println("请选择文件");
                    JOptionPane.showMessageDialog(null, "请选择文件");
                }
            }
        });

        jphome.add(jf);
        for (JButton j : jb)
            jphome.add(j);

        this.setContentPane(jphome);
        this.jfc.addActionListener(this);
        this.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        this.jpjfc.setVisible(false);
        this.setContentPane(jphome);
        this.jphome.setVisible(true);
        File file = jfc.getSelectedFile();
        String str = file.getPath();
        this.jf.setText(str);
    }
}
