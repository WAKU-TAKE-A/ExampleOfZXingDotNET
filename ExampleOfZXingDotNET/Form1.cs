using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ExampleOfZXingDotNET
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            Bitmap img = new Bitmap("qrcode.gif");

            ZXing.BarcodeReader reader = new ZXing.BarcodeReader();
            ZXing.Result result = reader.Decode(img);

            if (result != null)
            {
                textBox1.Text = result.BarcodeFormat.ToString();
                textBox2.Text = result.Text;
            }
        }
    }
}
