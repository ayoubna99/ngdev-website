// server.js

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();

// Static files (index.html, style.css, script.js, assets)
app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// POST /send-email -> called from front-end
app.post("/send-email", async (req, res) => {
  const { name, email, message } = req.body;

  if (!name || !email || !message) {
    return res.status(400).json({ ok: false, error: "Missing fields" });
  }

  // Configure SMTP transporter (Gmail example)
  const transporter = nodemailer.createTransport({
    host: "smtp.gmail.com",
    port: 587,
    secure: false,
    auth: {
      user: "business@ngdev.org", // your SMTP email
      pass: "YOUR_APP_PASSWORD_HERE", // app password / smtp password
    },
  });

  const mailOptions = {
    from: `"${name}" <${email}>`,
    to: "your_email@example.com", // where you receive messages
    subject: "New Contact Form Submission - NG Development",
    text: `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`,
  };

  try {
    await transporter.sendMail(mailOptions);
    res.json({ ok: true });
  } catch (error) {
    console.error("Error sending email:", error);
    res.status(500).json({ ok: false, error: "Failed to send" });
  }
});

// Optional: serve index.html on root
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
