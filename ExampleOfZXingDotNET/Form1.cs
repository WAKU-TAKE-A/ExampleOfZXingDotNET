using System;
using System.Drawing;
using System.Windows.Forms;
using System.IO;
using ZXing;
using ZXing.Windows.Compatibility;

namespace ExampleOfZXingDotNET
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            string imagePath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "examples", "qrcode.gif");

            if (File.Exists(imagePath))
            {
                using (Bitmap img = new Bitmap(imagePath))
                {
                    // Compatibility版のReaderを使用して.NET 8でのジェネリックエラーを回避
                    var reader = new BarcodeReader();
                    var result = reader.Decode(img);

                    if (result != null)
                    {
                        textBox1.Text = result.BarcodeFormat.ToString();
                        textBox2.Text = result.Text;
                    }
                }
            }
        }
    }
}
