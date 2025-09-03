from .base_otp import BaseOtpEmailSender

class LoginOtpSender(BaseOtpEmailSender):
    def __init__(self, email):
        super().__init__(email, purpose="login")

    def send(self):
        otp = self.generate_otp()
        subject = "✍️ Blogify - Secure Login Verification"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Blogify Login Authentication</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
                
                @keyframes fadeInUp {{
                    from {{ 
                        transform: translateY(30px); 
                        opacity: 0; 
                    }}
                    to {{ 
                        transform: translateY(0); 
                        opacity: 1; 
                    }}
                }}
                
                @keyframes pulse {{
                    0%, 100% {{ 
                        transform: scale(1); 
                        box-shadow: 0 0 0 0 rgba(139, 92, 246, 0.7);
                    }}
                    50% {{ 
                        transform: scale(1.05); 
                        box-shadow: 0 0 0 15px rgba(139, 92, 246, 0);
                    }}
                }}
                
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                
                body {{
                    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                    background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c);
                    background-size: 400% 400%;
                    margin: 0;
                    padding: 20px;
                }}
                
                .email-container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background: white;
                    border-radius: 20px;
                    overflow: hidden;
                    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
                    animation: fadeInUp 0.8s ease-out;
                }}
                
                .header {{
                    background: linear-gradient(135deg, #8B5CF6 0%, #A855F7 25%, #C084FC 50%, #7C3AED 75%, #6D28D9 100%);
                    padding: 40px 30px;
                    text-align: center;
                    position: relative;
                    overflow: hidden;
                }}
                
                .logo {{
                    position: relative;
                    z-index: 1;
                    font-size: 32px;
                    font-weight: 700;
                    color: white;
                    margin-bottom: 10px;
                    letter-spacing: -0.5px;
                }}
                
                .tagline {{
                    position: relative;
                    z-index: 1;
                    color: rgba(255, 255, 255, 0.9);
                    font-size: 16px;
                    font-weight: 400;
                    letter-spacing: 0.5px;
                }}
                
                .content {{
                    padding: 50px 40px;
                    background: white;
                }}
                
                .security-icon {{
                    width: 80px;
                    height: 80px;
                    background: linear-gradient(135deg, #8B5CF6, #A855F7);
                    border-radius: 50%;
                    margin: 0 auto 30px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 36px;
                    animation: pulse 2s infinite;
                }}
                
                .title {{
                    color: #1F2937;
                    font-size: 28px;
                    font-weight: 700;
                    text-align: center;
                    margin-bottom: 16px;
                    letter-spacing: -0.5px;
                }}
                
                .subtitle {{
                    color: #6B7280;
                    font-size: 16px;
                    text-align: center;
                    margin-bottom: 40px;
                    line-height: 1.6;
                }}
                
                .otp-container {{
                    background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
                    border: 2px solid #E2E8F0;
                    border-radius: 16px;
                    padding: 32px;
                    margin: 40px 0;
                    text-align: center;
                    position: relative;
                    overflow: hidden;
                }}
                
                .otp-container::before {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    height: 4px;
                    background: linear-gradient(90deg, #8B5CF6, #A855F7, #C084FC);
                }}
                
                .otp-label {{
                    color: #374151;
                    font-size: 12px;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    margin-bottom: 16px;
                }}
                
                .otp-code {{
                    font-size: 40px;
                    font-weight: 700;
                    color: #8B5CF6;
                    letter-spacing: 8px;
                    font-family: 'Monaco', 'Menlo', monospace;
                    margin: 0;
                    text-shadow: 0 2px 4px rgba(139, 92, 246, 0.2);
                }}
                
                .security-tips {{
                    background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
                    border-left: 4px solid #F59E0B;
                    border-radius: 8px;
                    padding: 24px;
                    margin: 32px 0;
                }}
                
                .tips-title {{
                    display: flex;
                    align-items: center;
                    color: #92400E;
                    font-weight: 600;
                    font-size: 14px;
                    margin-bottom: 12px;
                }}
                
                .tips-list {{
                    color: #78350F;
                    font-size: 14px;
                    line-height: 1.6;
                    margin: 0;
                    padding-left: 20px;
                }}
                
                .footer {{
                    background: #F9FAFB;
                    padding: 32px;
                    text-align: center;
                    border-top: 1px solid #E5E7EB;
                }}
                
                .footer-text {{
                    color: #6B7280;
                    font-size: 14px;
                    margin-bottom: 16px;
                }}
                
                .copyright {{
                    color: #9CA3AF;
                    font-size: 12px;
                    margin-top: 16px;
                }}
                
                @media (max-width: 600px) {{
                    body {{ padding: 10px; }}
                    .content {{ padding: 30px 20px; }}
                    .title {{ font-size: 24px; }}
                    .otp-code {{ font-size: 32px; letter-spacing: 4px; }}
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <div class="logo">✍️ Blogify</div>
                    <div class="tagline">Where Stories Come to Life</div>
                </div>
                
                <div class="content">
                    <div class="security-icon">🔐</div>
                    
                    <h1 class="title">Secure Login Verification</h1>
                    <p class="subtitle">
                        Welcome back to Blogify! We've detected a login attempt on your account. 
                        Please verify your identity with the code below to continue to your dashboard.
                    </p>
                    
                    <div class="otp-container">
                        <div class="otp-label">Your Verification Code</div>
                        <div class="otp-code">{otp}</div>
                    </div>
                    
                    <div class="security-tips">
                        <div class="tips-title">
                            🛡️ Security Best Practices
                        </div>
                        <ul class="tips-list">
                            <li>This code expires in <strong>10 minutes</strong> for your security</li>
                            <li>Never share this code with anyone, including Blogify support</li>
                            <li>If you didn't request this, please secure your account immediately</li>
                        </ul>
                    </div>
                    
                    <p style="color: #6B7280; font-size: 14px; text-align: center; line-height: 1.6; margin-top: 40px;">
                        This login attempt was made from a new device or location. If this wasn't you, 
                        please <a href="#" style="color: #8B5CF6; text-decoration: none;">secure your account</a> 
                        and contact our support team.
                    </p>
                </div>
                
                <div class="footer">
                    <p class="footer-text">
                        Need help? Contact us at 
                        <a href="mailto:support@blogify.com" style="color: #8B5CF6; text-decoration: none;">support@blogify.com</a>
                    </p>
                    <p class="copyright">
                        © 2025 Blogify. All rights reserved. | 
                        <a href="#" style="color: #9CA3AF; text-decoration: none;">Privacy Policy</a> | 
                        <a href="#" style="color: #9CA3AF; text-decoration: none;">Terms of Service</a>
                    </p>
                </div>
            </div>
        </body>
        </html>
        """
        
        text_content = f"""
        BLOGIFY - SECURE LOGIN VERIFICATION
        =====================================
        
        Welcome back to Blogify!
        
        Your verification code is: {otp}
        
        This code expires in 10 minutes for your security.
        
        SECURITY TIPS:
        • Never share this code with anyone
        • If you didn't request this login, secure your account immediately
        • Contact support@blogify.com if you need assistance
        
        Happy blogging!
        The Blogify Team
        
        ---
        © 2025 Blogify. All rights reserved.
        """

        self.send_email(subject, text_content, html_content=html_content)
        return otp


class ForgetPasswordOtpSender(BaseOtpEmailSender):
    def __init__(self, email):
        super().__init__(email, purpose="forget")

    def send(self):
        otp = self.generate_otp()
        subject = "🔑 Blogify - Password Reset Verification"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Blogify Password Reset</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
                
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                
                body {{
                    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                    background: linear-gradient(-45deg, #ef4444, #f97316, #eab308, #ef4444);
                    background-size: 400% 400%;
                    margin: 0;
                    padding: 20px;
                }}
                
                .email-container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background: white;
                    border-radius: 20px;
                    overflow: hidden;
                    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
                }}
                
                .header {{
                    background: linear-gradient(135deg, #EF4444 0%, #F97316 25%, #EAB308 50%, #F59E0B 75%, #DC2626 100%);
                    padding: 40px 30px;
                    text-align: center;
                    color: white;
                }}
                
                .logo {{
                    font-size: 32px;
                    font-weight: 700;
                    margin-bottom: 10px;
                    letter-spacing: -0.5px;
                }}
                
                .tagline {{
                    font-size: 16px;
                    font-weight: 400;
                    letter-spacing: 0.5px;
                }}
                
                .content {{
                    padding: 50px 40px;
                }}
                
                .reset-icon {{
                    width: 80px;
                    height: 80px;
                    background: linear-gradient(135deg, #EF4444, #F97316);
                    border-radius: 50%;
                    margin: 0 auto 30px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 36px;
                }}
                
                .title {{
                    color: #1F2937;
                    font-size: 28px;
                    font-weight: 700;
                    text-align: center;
                    margin-bottom: 16px;
                }}
                
                .subtitle {{
                    color: #6B7280;
                    font-size: 16px;
                    text-align: center;
                    margin-bottom: 40px;
                    line-height: 1.6;
                }}
                
                .otp-container {{
                    background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
                    border: 2px solid #FECACA;
                    border-radius: 16px;
                    padding: 32px;
                    margin: 40px 0;
                    text-align: center;
                }}
                
                .otp-label {{
                    color: #7F1D1D;
                    font-size: 12px;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    margin-bottom: 16px;
                }}
                
                .otp-code {{
                    font-size: 40px;
                    font-weight: 700;
                    color: #EF4444;
                    letter-spacing: 8px;
                    font-family: 'Monaco', 'Menlo', monospace;
                    margin: 0;
                }}
                
                .warning-section {{
                    background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
                    border-left: 4px solid #F59E0B;
                    border-radius: 8px;
                    padding: 24px;
                    margin: 32px 0;
                }}
                
                .warning-title {{
                    color: #92400E;
                    font-weight: 600;
                    font-size: 14px;
                    margin-bottom: 12px;
                }}
                
                .warning-text {{
                    color: #78350F;
                    font-size: 14px;
                    line-height: 1.6;
                    margin: 0;
                }}
                
                .footer {{
                    background: #F9FAFB;
                    padding: 32px;
                    text-align: center;
                    border-top: 1px solid #E5E7EB;
                    color: #6B7280;
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <div class="logo">🔑 Blogify</div>
                    <div class="tagline">Password Recovery Service</div>
                </div>
                
                <div class="content">
                    <div class="reset-icon">🔓</div>
                    
                    <h1 class="title">Reset Your Password</h1>
                    <p class="subtitle">
                        Don't worry, it happens to the best of us! We've received a request to reset your 
                        Blogify account password. Use the verification code below to create a new password.
                    </p>
                    
                    <div class="otp-container">
                        <div class="otp-label">Password Reset Code</div>
                        <div class="otp-code">{otp}</div>
                    </div>
                    
                    <div class="warning-section">
                        <div class="warning-title">
                            ⚠️ Important Security Notice
                        </div>
                        <p class="warning-text">
                            If you didn't request this password reset, please ignore this email and contact our 
                            security team immediately. This verification code expires in <strong>10 minutes</strong> 
                            and can only be used once for your protection.
                        </p>
                    </div>
                </div>
                
                <div class="footer">
                    <p>
                        Need help? Contact us at 
                        <a href="mailto:support@blogify.com" style="color: #EF4444; text-decoration: none;">support@blogify.com</a>
                    </p>
                    <p style="margin-top: 16px; color: #9CA3AF; font-size: 12px;">
                        © 2025 Blogify. All rights reserved.
                    </p>
                </div>
            </div>
        </body>
        </html>
        """
        
        text_content = f"""
        BLOGIFY - PASSWORD RESET VERIFICATION
        =====================================
        
        Password Reset Request
        
        Your verification code is: {otp}
        
        SECURITY NOTICE:
        • This code expires in 10 minutes
        • If you didn't request this reset, contact support immediately
        • The code can only be used once for your protection
        
        Need help? Contact support@blogify.com
        
        ---
        © 2025 Blogify. All rights reserved.
        """

        self.send_email(subject, text_content, html_content=html_content)
        return otp


class WelcomeEmailSender(BaseOtpEmailSender):
    def __init__(self, email, username):
        super().__init__(email, purpose="welcome")
        self.username = username

    def send(self):
        subject = "🎉 Welcome to Blogify - Your Writing Journey Begins!"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Blogify</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
                
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                
                body {{
                    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                    background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #f5576c);
                    background-size: 400% 400%;
                    margin: 0;
                    padding: 20px;
                }}
                
                .email-container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background: white;
                    border-radius: 20px;
                    overflow: hidden;
                    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
                }}
                
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 50px 30px;
                    text-align: center;
                    color: white;
                }}
                
                .logo {{
                    font-size: 36px;
                    font-weight: 700;
                    margin-bottom: 15px;
                }}
                
                .welcome-text {{
                    font-size: 20px;
                    font-weight: 500;
                }}
                
                .content {{
                    padding: 50px 40px;
                }}
                
                .greeting {{
                    font-size: 28px;
                    font-weight: 700;
                    color: #1F2937;
                    text-align: center;
                    margin-bottom: 20px;
                }}
                
                .intro-text {{
                    font-size: 16px;
                    color: #6B7280;
                    text-align: center;
                    line-height: 1.7;
                    margin-bottom: 40px;
                }}
                
                .feature-grid {{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 20px;
                    margin: 40px 0;
                }}
                
                .feature-card {{
                    background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
                    padding: 24px;
                    border-radius: 12px;
                    text-align: center;
                    border: 1px solid #E2E8F0;
                }}
                
                .feature-icon {{
                    font-size: 32px;
                    margin-bottom: 12px;
                }}
                
                .feature-title {{
                    font-size: 16px;
                    font-weight: 600;
                    color: #374151;
                    margin-bottom: 8px;
                }}
                
                .feature-desc {{
                    font-size: 14px;
                    color: #6B7280;
                    line-height: 1.5;
                }}
                
                .footer {{
                    background: #F9FAFB;
                    padding: 32px;
                    text-align: center;
                    border-top: 1px solid #E5E7EB;
                    color: #6B7280;
                    font-size: 14px;
                }}
                
                @media (max-width: 600px) {{
                    .feature-grid {{ grid-template-columns: 1fr; }}
                    .content {{ padding: 30px 20px; }}
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <div class="logo">✍️ Blogify</div>
                    <div class="welcome-text">Welcome to the Community!</div>
                </div>
                
                <div class="content">
                    <h1 class="greeting">Hello {self.username}! 👋</h1>
                    <p class="intro-text">
                        Welcome to Blogify, where your stories come to life! We're thrilled to have you join our 
                        community of passionate writers, creators, and storytellers. Your writing journey starts now!
                    </p>
                    
                    <div class="feature-grid">
                        <div class="feature-card">
                            <div class="feature-icon">✍️</div>
                            <div class="feature-title">Rich Editor</div>
                            <div class="feature-desc">Create beautiful posts with our intuitive writing tools</div>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">🌍</div>
                            <div class="feature-title">Global Reach</div>
                            <div class="feature-desc">Share your stories with readers worldwide</div>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">📈</div>
                            <div class="feature-title">Analytics</div>
                            <div class="feature-desc">Track your content performance and engagement</div>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">👥</div>
                            <div class="feature-title">Community</div>
                            <div class="feature-desc">Connect with fellow writers and readers</div>
                        </div>
                    </div>
                </div>
                
                <div class="footer">
                    <p>
                        Questions? We're here to help! Contact us at 
                        <a href="mailto:support@blogify.com" style="color: #667eea; text-decoration: none;">support@blogify.com</a>
                    </p>
                    <p style="margin-top: 16px; color: #9CA3AF; font-size: 12px;">
                        © 2025 Blogify. All rights reserved.
                    </p>
                </div>
            </div>
        </body>
        </html>
        """
        
        text_content = f"""
        WELCOME TO BLOGIFY!
        ===================
        
        Hello {self.username}!
        
        Welcome to Blogify, where your stories come to life! We're thrilled to have you 
        join our community of passionate writers and creators.
        
        WHAT YOU CAN DO:
        • Create beautiful posts with our rich editor
        • Share your stories with readers worldwide  
        • Track your content performance
        • Connect with fellow writers
        
        Ready to start writing? Visit your dashboard and create your first post!
        
        Questions? Contact us at support@blogify.com
        
        Happy writing!
        The Blogify Team
        
        ---
        © 2025 Blogify. All rights reserved.
        """

        self.send_email(subject, text_content, html_content=html_content)
        return "Welcome email sent successfully!"





class RegistrationOtpSender(BaseOtpEmailSender):
    def __init__(self,email):
        super().__init__(email,purpose="register")


    def send(self):
        otp = self.generate_otp()
        subject = "📧 Sākṣin - Account Verification Required"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Account Verification</title>
            <style>
                @keyframes slideDown {{
                    from {{ transform: translateY(-20px); opacity: 0; }}
                    to {{ transform: translateY(0); opacity: 1; }}
                }}
                @keyframes subtlePulse {{
                    0%, 100% {{ transform: scale(1); }}
                    50% {{ transform: scale(1.02); }}
                }}
                .container {{
                    max-width: 650px;
                    margin: 0 auto;
                    background: #f5f7fa;
                    font-family: 'Arial', sans-serif;
                    padding: 0;
                }}
                .header {{
                    background: linear-gradient(135deg, #2b6cb0 0%, #3182ce 100%);
                    padding: 40px 30px;
                    text-align: center;
                    color: white;
                }}
                .logo {{
                    font-size: 28px;
                    font-weight: 600;
                    margin-bottom: 8px;
                    letter-spacing: 1px;
                }}
                .subtitle {{
                    font-size: 16px;
                    opacity: 0.9;
                    font-weight: 300;
                }}
                .content {{
                    background: white;
                    padding: 50px 40px;
                    animation: slideDown 0.6s ease-out;
                }}
                .verify-badge {{
                    width: 60px;
                    height: 60px;
                    background: linear-gradient(135deg, #2b6cb0, #3182ce);
                    border-radius: 50%;
                    margin: 0 auto 30px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 24px;
                    color: white;
                    animation: subtlePulse 3s infinite;
                }}
                .title {{
                    color: #2b6cb0;
                    font-size: 24px;
                    font-weight: 600;
                    margin: 0 0 20px 0;
                    text-align: center;
                }}
                .description {{
                    color: #4a5568;
                    font-size: 16px;
                    line-height: 1.6;
                    text-align: center;
                    margin-bottom: 35px;
                }}
                .otp-section {{
                    background: linear-gradient(135deg, #ebf8ff 0%, #bee3f8 100%);
                    border: 2px solid #90cdf4;
                    border-radius: 12px;
                    padding: 30px;
                    margin: 30px 0;
                    text-align: center;
                }}
                .otp-label {{
                    color: #2c5282;
                    font-size: 14px;
                    font-weight: 500;
                    margin-bottom: 15px;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }}
                .otp {{
                    font-size: 32px;
                    font-weight: 700;
                    color: #2b6cb0;
                    letter-spacing: 6px;
                    font-family: 'Courier New', monospace;
                    margin: 0;
                }}
                .progress-section {{
                    background: #f7fafc;
                    border-radius: 8px;
                    padding: 25px;
                    margin: 30px 0;
                }}
                .progress-title {{
                    color: #2d3748;
                    font-weight: 600;
                    margin-bottom: 20px;
                    font-size: 16px;
                    text-align: center;
                }}
                .progress-steps {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    position: relative;
                }}
                .progress-step {{
                    text-align: center;
                    flex: 1;
                }}
                .step-circle {{
                    width: 36px;
                    height: 36px;
                    border-radius: 50%;
                    margin: 0 auto 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-weight: 600;
                    font-size: 14px;
                }}
                .step-completed {{
                    background: #48bb78;
                    color: white;
                }}
                .step-active {{
                    background: #3182ce;
                    color: white;
                }}
                .step-pending {{
                    background: #e2e8f0;
                    color: #a0aec0;
                }}
                .step-text {{
                    font-size: 12px;
                    color: #718096;
                    font-weight: 500;
                }}
                .progress-line {{
                    position: absolute;
                    top: 18px;
                    left: 25%;
                    right: 25%;
                    height: 2px;
                    background: #e2e8f0;
                    z-index: 1;
                }}
                .progress-fill {{
                    height: 100%;
                    background: #48bb78;
                    width: 50%;
                }}
                .welcome-notice {{
                    background: #f0fff4;
                    border-left: 4px solid #48bb78;
                    border-radius: 6px;
                    padding: 20px;
                    margin: 30px 0;
                }}
                .notice-title {{
                    color: #276749;
                    font-weight: 600;
                    margin-bottom: 8px;
                    font-size: 14px;
                }}
                .notice-text {{
                    color: #2f855a;
                    font-size: 14px;
                    margin: 0;
                }}
                .features {{
                    background: #f7fafc;
                    border-radius: 8px;
                    padding: 25px;
                    margin: 30px 0;
                }}
                .feature {{
                    display: flex;
                    align-items: center;
                    margin-bottom: 12px;
                    font-size: 14px;
                    color: #4a5568;
                }}
                .feature-icon {{
                    margin-right: 12px;
                    font-size: 16px;
                }}
                .footer {{
                    background: #2d3748;
                    color: #a0aec0;
                    padding: 30px;
                    text-align: center;
                    font-size: 14px;
                }}
                .footer-link {{
                    color: #63b3ed;
                    text-decoration: none;
                }}
                .divider {{
                    height: 1px;
                    background: #e2e8f0;
                    margin: 30px 0;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <div class="logo">📧 Sākṣin</div>
                    <div class="subtitle">Professional Interview Platform</div>
                </div>
                <div class="content">
                    <div class="verify-badge">✓</div>
                    <h1 class="title">Complete Your Registration</h1>
                    <p class="description">
                        Welcome to Sākṣin! You're one step away from accessing our professional interview platform. Please verify your email address using the code below.
                    </p>
                    
                    <div class="progress-section">
                        <div class="progress-title">Registration Progress</div>
                        <div class="progress-steps">
                            <div class="progress-line">
                                <div class="progress-fill"></div>
                            </div>
                            <div class="progress-step">
                                <div class="step-circle step-completed">✓</div>
                                <div class="step-text">Account Created</div>
                            </div>
                            <div class="progress-step">
                                <div class="step-circle step-active">2</div>
                                <div class="step-text">Email Verification</div>
                            </div>
                            <div class="progress-step">
                                <div class="step-circle step-pending">3</div>
                                <div class="step-text">Complete Setup</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="otp-section">
                        <div class="otp-label">Verification Code</div>
                        <div class="otp">{otp}</div>
                    </div>
                    
                    <div class="features">
                        <h3 style="color: #2d3748; margin: 0 0 20px 0; font-size: 16px;">What's waiting for you:</h3>
                        <div class="feature">
                            <div class="feature-icon">🎯</div>
                            <span>AI-powered interview simulations</span>
                        </div>
                        <div class="feature">
                            <div class="feature-icon">📊</div>
                            <span>Detailed performance analytics</span>
                        </div>
                        <div class="feature">
                            <div class="feature-icon">🏆</div>
                            <span>Industry-specific question banks</span>
                        </div>
                        <div class="feature">
                            <div class="feature-icon">📈</div>
                            <span>Progress tracking and improvement insights</span>
                        </div>
                    </div>
                    
                    <div class="welcome-notice">
                        <div class="notice-title">🎯 Professional Development</div>
                        <p class="notice-text">This verification code expires in 10 minutes. Keep this information confidential and secure.</p>
                    </div>
                    
                    <div class="divider"></div>
                    
                    <p style="color: #718096; font-size: 14px; text-align: center; margin: 0;">
                        If you didn't create this account, please ignore this email or contact our support team.
                    </p>
                </div>
                <div class="footer">
                    <p>© 2025 Sākṣin. All rights reserved.</p>
                    <p>Support: <a href="mailto:support@saksin.ai" class="footer-link">support@saksin.ai</a></p>
                    <p style="margin-top: 15px; font-size: 12px;">
                        <a href="#" class="footer-link">Privacy Policy</a> | 
                        <a href="#" class="footer-link">Terms of Service</a> | 
                        <a href="#" class="footer-link">Help Center</a>
                    </p>
                </div>
            </div>
        </body>
        </html>
        """
        
        text_content = f"""
        WELCOME TO BLOGIFY!
        ===================
        
        Hello {self.username}!
        
        Welcome to Blogify, where your stories come to life! We're thrilled to have you 
        join our community of passionate writers and creators.
        
        WHAT YOU CAN DO:
        • Create beautiful posts with our rich editor
        • Share your stories with readers worldwide  
        • Track your content performance
        • Connect with fellow writers
        
        Ready to start writing? Visit your dashboard and create your first post!
        
        Questions? Contact us at support@blogify.com
        
        Happy writing!
        The Blogify Team
        
        ---
        © 2025 Blogify. All rights reserved.
        """

        self.send_email(subject, text_content, html_content=html_content)
        return "Welcome email sent successfully!"


class RegistrationOtpSender(BaseOtpEmailSender):
    def __init__(self, email):
        super().__init__(email, purpose="register")

    def send(self):
        otp = self.generate_otp()
        subject = "🚀 Welcome to Blogify - Verify Your Account"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Blogify Registration</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
                
                @keyframes fadeInUp {{
                    from {{ 
                        transform: translateY(30px); 
                        opacity: 0; 
                    }}
                    to {{ 
                        transform: translateY(0); 
                        opacity: 1; 
                    }}
                }}
                
                @keyframes pulse {{
                    0%, 100% {{ 
                        transform: scale(1); 
                        box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7);
                    }}
                    50% {{ 
                        transform: scale(1.05); 
                        box-shadow: 0 0 0 15px rgba(34, 197, 94, 0);
                    }}
                }}
                
                @keyframes sparkle {{
                    0% {{ transform: rotate(0deg) scale(1); }}
                    50% {{ transform: rotate(180deg) scale(1.1); }}
                    100% {{ transform: rotate(360deg) scale(1); }}
                }}
                
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                
                body {{
                    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                    background: linear-gradient(-45deg, #22c55e, #16a34a, #15803d, #14532d);
                    background-size: 400% 400%;
                    margin: 0;
                    padding: 20px;
                }}
                
                .email-container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background: white;
                    border-radius: 20px;
                    overflow: hidden;
                    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
                    animation: fadeInUp 0.8s ease-out;
                }}
                
                .header {{
                    background: linear-gradient(135deg, #22C55E 0%, #16A34A 25%, #15803D 50%, #14532D 75%, #166534 100%);
                    padding: 40px 30px;
                    text-align: center;
                    position: relative;
                    overflow: hidden;
                }}
                
                .sparkle {{
                    position: absolute;
                    color: rgba(255, 255, 255, 0.6);
                    font-size: 16px;
                    animation: sparkle 3s infinite;
                }}
                
                .sparkle:nth-child(1) {{ top: 20%; left: 15%; animation-delay: 0s; }}
                .sparkle:nth-child(2) {{ top: 30%; right: 20%; animation-delay: 1s; }}
                .sparkle:nth-child(3) {{ bottom: 30%; left: 20%; animation-delay: 2s; }}
                .sparkle:nth-child(4) {{ bottom: 20%; right: 15%; animation-delay: 0.5s; }}
                
                .logo {{
                    position: relative;
                    z-index: 1;
                    font-size: 32px;
                    font-weight: 700;
                    color: white;
                    margin-bottom: 10px;
                    letter-spacing: -0.5px;
                }}
                
                .tagline {{
                    position: relative;
                    z-index: 1;
                    color: rgba(255, 255, 255, 0.9);
                    font-size: 16px;
                    font-weight: 400;
                    letter-spacing: 0.5px;
                }}
                
                .content {{
                    padding: 50px 40px;
                    background: white;
                }}
                
                .verification-icon {{
                    width: 80px;
                    height: 80px;
                    background: linear-gradient(135deg, #22C55E, #16A34A);
                    border-radius: 50%;
                    margin: 0 auto 30px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 36px;
                    animation: pulse 2s infinite;
                }}
                
                .title {{
                    color: #1F2937;
                    font-size: 28px;
                    font-weight: 700;
                    text-align: center;
                    margin-bottom: 16px;
                    letter-spacing: -0.5px;
                }}
                
                .subtitle {{
                    color: #6B7280;
                    font-size: 16px;
                    text-align: center;
                    margin-bottom: 40px;
                    line-height: 1.6;
                }}
                
                .otp-container {{
                    background: linear-gradient(135deg, #F0FDF4 0%, #DCFCE7 100%);
                    border: 2px solid #BBF7D0;
                    border-radius: 16px;
                    padding: 32px;
                    margin: 40px 0;
                    text-align: center;
                    position: relative;
                    overflow: hidden;
                }}
                
                .otp-container::before {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    height: 4px;
                    background: linear-gradient(90deg, #22C55E, #16A34A, #15803D);
                }}
                
                .otp-label {{
                    color: #166534;
                    font-size: 12px;
                    font-weight: 600;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    margin-bottom: 16px;
                }}
                
                .otp-code {{
                    font-size: 40px;
                    font-weight: 700;
                    color: #22C55E;
                    letter-spacing: 8px;
                    font-family: 'Monaco', 'Menlo', monospace;
                    margin: 0;
                    text-shadow: 0 2px 4px rgba(34, 197, 94, 0.2);
                }}
                
                .welcome-section {{
                    background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
                    border-radius: 12px;
                    padding: 28px;
                    margin: 32px 0;
                    text-align: center;
                }}
                
                .welcome-title {{
                    color: #1E40AF;
                    font-weight: 600;
                    font-size: 18px;
                    margin-bottom: 16px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
                
                .benefits-list {{
                    color: #1D4ED8;
                    font-size: 14px;
                    line-height: 1.8;
                    text-align: left;
                    max-width: 400px;
                    margin: 0 auto;
                }}
                
                .benefits-list li {{
                    margin-bottom: 8px;
                    padding-left: 8px;
                }}
                
                .security-note {{
                    background: linear-gradient(135deg, #FEF3C7 0%, #FDE68A 100%);
                    border-left: 4px solid #F59E0B;
                    border-radius: 8px;
                    padding: 20px;
                    margin: 32px 0;
                }}
                
                .note-title {{
                    display: flex;
                    align-items: center;
                    color: #92400E;
                    font-weight: 600;
                    font-size: 14px;
                    margin-bottom: 8px;
                }}
                
                .note-text {{
                    color: #78350F;
                    font-size: 14px;
                    line-height: 1.6;
                    margin: 0;
                }}
                
                .cta-section {{
                    text-align: center;
                    margin: 40px 0;
                }}
                
                .cta-button {{
                    display: inline-block;
                    background: linear-gradient(135deg, #22C55E, #16A34A);
                    color: white;
                    padding: 16px 32px;
                    text-decoration: none;
                    border-radius: 12px;
                    font-weight: 600;
                    font-size: 16px;
                    letter-spacing: 0.5px;
                    transition: all 0.3s ease;
                    box-shadow: 0 4px 15px rgba(34, 197, 94, 0.4);
                }}
                
                .cta-button:hover {{
                    transform: translateY(-2px);
                    box-shadow: 0 8px 25px rgba(34, 197, 94, 0.5);
                }}
                
                .footer {{
                    background: #F9FAFB;
                    padding: 32px;
                    text-align: center;
                    border-top: 1px solid #E5E7EB;
                }}
                
                .footer-text {{
                    color: #6B7280;
                    font-size: 14px;
                    margin-bottom: 16px;
                }}
                
                .social-links {{
                    display: flex;
                    justify-content: center;
                    gap: 16px;
                    margin-bottom: 20px;
                }}
                
                .social-link {{
                    width: 40px;
                    height: 40px;
                    background: #E5E7EB;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    text-decoration: none;
                    color: #6B7280;
                    transition: all 0.3s ease;
                }}
                
                .social-link:hover {{
                    background: #22C55E;
                    color: white;
                    transform: translateY(-2px);
                }}
                
                .copyright {{
                    color: #9CA3AF;
                    font-size: 12px;
                    margin-top: 16px;
                }}
                
                @media (max-width: 600px) {{
                    body {{ padding: 10px; }}
                    .content {{ padding: 30px 20px; }}
                    .title {{ font-size: 24px; }}
                    .otp-code {{ font-size: 32px; letter-spacing: 4px; }}
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <div class="sparkle">✨</div>
                    <div class="sparkle">⭐</div>
                    <div class="sparkle">💫</div>
                    <div class="sparkle">🌟</div>
                    
                    <div class="logo">🚀 Blogify</div>
                    <div class="tagline">Account Verification</div>
                </div>
                
                <div class="content">
                    <div class="verification-icon">✅</div>
                    
                    <h1 class="title">Almost There!</h1>
                    <p class="subtitle">
                        Thank you for joining Blogify! You're just one step away from unlocking your creative potential. 
                        Please verify your email address using the code below to complete your registration.
                    </p>
                    
                    <div class="otp-container">
                        <div class="otp-label">Verification Code</div>
                        <div class="otp-code">{otp}</div>
                    </div>
                    
                    <div class="welcome-section">
                        <div class="welcome-title">
                            🎯 What awaits you in Blogify:
                        </div>
                        <ul class="benefits-list">
                            <li>✍️ <strong>Powerful Editor:</strong> Write with our intuitive, feature-rich editor</li>
                            <li>🌐 <strong>Global Audience:</strong> Reach readers from around the world</li>
                            <li>📊 <strong>Analytics Dashboard:</strong> Track your content's performance</li>
                            <li>👥 <strong>Writer Community:</strong> Connect with fellow creators</li>
                            <li>🎨 <strong>Customization:</strong> Personalize your author profile</li>
                        </ul>
                    </div>
                    
                    <div class="security-note">
                        <div class="note-title">
                            🔒 Security Information
                        </div>
                        <p class="note-text">
                            This verification code expires in <strong>10 minutes</strong> for your security. 
                            If you didn't create this account, please ignore this email. Your information is safe with us.
                        </p>
                    </div>
                    
                    <div class="cta-section">
                        <a href="#" class="cta-button">Verify & Start Writing</a>
                    </div>
                    
                    <p style="color: #6B7280; font-size: 14px; text-align: center; line-height: 1.6; margin-top: 30px;">
                        After verification, you'll be redirected to your dashboard where you can start creating amazing content. 
                        Need help? Our support team is ready to assist you at any time.
                    </p>
                </div>
                
                <div class="footer">
                    <div class="social-links">
                        <a href="#" class="social-link">📧</a>
                        <a href="#" class="social-link">🐦</a>
                        <a href="#" class="social-link">📘</a>
                        <a href="#" class="social-link">📱</a>
                    </div>
                    <p class="footer-text">
                        Questions? Contact us at 
                        <a href="mailto:support@blogify.com" style="color: #22C55E; text-decoration: none;">support@blogify.com</a>
                    </p>
                    <p class="copyright">
                        © 2025 Blogify. All rights reserved. | 
                        <a href="#" style="color: #9CA3AF; text-decoration: none;">Privacy Policy</a> | 
                        <a href="#" style="color: #9CA3AF; text-decoration: none;">Terms of Service</a>
                    </p>
                </div>
            </div>
        </body>
        </html>
        """
        
        text_content = f"""
        BLOGIFY - ACCOUNT VERIFICATION
        ==============================
        
        Welcome to Blogify!
        
        Your verification code is: {otp}
        
        Please use this code to complete your account registration.
        
        WHAT AWAITS YOU:
        • Powerful writing tools and editor
        • Global audience for your stories
        • Analytics to track your content performance
        • Connect with fellow writers and readers
        • Customizable author profile
        
        IMPORTANT:
        • This code expires in 10 minutes
        • If you didn't create this account, please ignore this email
        
        Questions? Contact support@blogify.com
        
        Welcome to the community!
        The Blogify Team
        
        ---
        © 2025 Blogify. All rights reserved.
        """

        self.send_email(subject, text_content, html_content=html_content)
        return otp