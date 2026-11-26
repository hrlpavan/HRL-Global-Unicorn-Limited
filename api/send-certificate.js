// Vercel Serverless Function: Official Certificate Email Dispatch via Resend
// Set RESEND_API_KEY (and optional FROM_EMAIL) in Vercel Project Environment Variables.

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, email, subject, subjectDuration, examDuration, percent, correct, total, certId, issueDate } = req.body || {};

  if (!name || !email || !certId || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return res.status(400).json({ error: 'Missing or invalid candidate details.' });
  }

  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    return res.status(503).json({
      sent: false,
      error: 'Email service not configured yet. Add RESEND_API_KEY in Vercel Environment Variables to enable automatic delivery.'
    });
  }

  const fromEmail = process.env.FROM_EMAIL || 'HRL International Certifications <onboarding@resend.dev>';
  const verifyUrl = `https://hrl-brand-seo.vercel.app/agentic-engineering-certification.html?verify=${encodeURIComponent(certId)}`;

  const html = `
    <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:640px;margin:0 auto;padding:32px;border:2px solid #121216;background:#ffffff;color:#1d1d1f;">
      <div style="border-bottom:2px solid #D1002D;padding-bottom:16px;margin-bottom:24px;">
        <div style="font-size:18px;font-weight:800;letter-spacing:0.04em;text-transform:uppercase;">HRL International Private Limited&trade;</div>
        <div style="font-size:12px;font-weight:700;color:#D1002D;letter-spacing:0.1em;text-transform:uppercase;margin-top:4px;">Official Corporate Certification Authority</div>
      </div>
      <p style="font-size:15px;margin:0 0 12px;">Dear <strong>${escapeHtml(name)}</strong>,</p>
      <p style="font-size:15px;line-height:1.6;color:#515154;margin:0 0 20px;">
        Congratulations on completing the official <strong>${escapeHtml(subjectDuration || '1 Hour')}</strong> corporate subject and passing the <strong>${escapeHtml(examDuration || '20 Minutes')}</strong> examination in:
      </p>
      <div style="background:#F5F5F7;border-left:4px solid #D1002D;padding:16px 20px;margin-bottom:24px;">
        <div style="font-size:18px;font-weight:800;color:#121216;margin-bottom:6px;">${escapeHtml(subject || 'Agentic Engineering with Context & Harness Engineering')}</div>
        <div style="font-size:13px;color:#515154;">
          Score: <strong>${escapeHtml(String(percent))}% (${escapeHtml(String(correct))}/${escapeHtml(String(total))})</strong> &middot;
          Certificate ID: <strong>${escapeHtml(certId)}</strong> &middot;
          Issued: <strong>${escapeHtml(issueDate || '')}</strong>
        </div>
      </div>
      <p style="margin:0 0 24px;">
        <a href="${verifyUrl}" style="display:inline-block;background:#D1002D;color:#ffffff;text-decoration:none;padding:12px 22px;border-radius:9999px;font-weight:700;font-size:14px;">View &amp; Verify Official Certificate</a>
      </p>
      <div style="border-top:1px solid #e5e5e7;padding-top:16px;font-size:12px;color:#86868b;">
        Issued by Pavan Kumar Sadashiv, Founder &amp; Managing Director, HRL International Private Limited.<br>
        <em>&ldquo;We Can Do Everything Related To Software Sector Without Any Excuses!&rdquo;</em>
      </div>
    </div>
  `;

  try {
    const response = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: fromEmail,
        to: [email],
        cc: ['hrlinternationalprivatelimited@gmail.com'],
        subject: `Official Certificate: Agentic Engineering with Context & Harness Engineering (${certId})`,
        html
      })
    });

    const data = await response.json();
    if (!response.ok) {
      return res.status(response.status).json({ sent: false, error: data.message || 'Resend API error' });
    }

    return res.status(200).json({ sent: true, id: data.id });
  } catch (err) {
    return res.status(500).json({ sent: false, error: 'Failed to dispatch certificate email.' });
  }
}

function escapeHtml(str) {
  return String(str).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}
