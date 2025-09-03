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
    def __init__(self, email):
        super().__init__(email, purpose="register")

    def send(self):
        otp = self.generate_otp()
        subject = "✨ Welcome to Blogify - Your Creative Journey Starts Here!"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Blogify</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');
                
                @keyframes fadeInUp {{
                    from {{ 
                        transform: translateY(40px); 
                        opacity: 0; 
                    }}
                    to {{ 
                        transform: translateY(0); 
                        opacity: 1; 
                    }}
                }}
                
                @keyframes slideInLeft {{
                    from {{ 
                        transform: translateX(-50px); 
                        opacity: 0; 
                    }}
                    to {{ 
                        transform: translateX(0); 
                        opacity: 1; 
                    }}
                }}
                
                @keyframes slideInRight {{
                    from {{ 
                        transform: translateX(50px); 
                        opacity: 0; 
                    }}
                    to {{ 
                        transform: translateX(0); 
                        opacity: 1; 
                    }}
                }}
                
                @keyframes glowPulse {{
                    0%, 100% {{ 
                        transform: scale(1); 
                        box-shadow: 0 0 20px rgba(99, 102, 241, 0.4), 0 0 40px rgba(99, 102, 241, 0.2);
                    }}
                    50% {{ 
                        transform: scale(1.03); 
                        box-shadow: 0 0 30px rgba(99, 102, 241, 0.6), 0 0 60px rgba(99, 102, 241, 0.3);
                    }}
                }}
                
                @keyframes floatingElements {{
                    0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
                    33% {{ transform: translateY(-10px) rotate(2deg); }}
                    66% {{ transform: translateY(5px) rotate(-2deg); }}
                }}
                
                @keyframes textShimmer {{
                    0% {{ background-position: -200% center; }}
                    100% {{ background-position: 200% center; }}
                }}
                
                @keyframes bounceIn {{
                    0% {{ transform: scale(0.3) rotate(-10deg); opacity: 0; }}
                    50% {{ transform: scale(1.05) rotate(5deg); }}
                    70% {{ transform: scale(0.9) rotate(-2deg); }}
                    100% {{ transform: scale(1) rotate(0deg); opacity: 1; }}
                }}
                
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                
                body {{
                    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                    background: linear-gradient(-45deg, #667eea, #764ba2, #667eea, #f093fb, #f5576c, #4facfe, #00f2fe);
                    background-size: 400% 400%;
                    animation: gradientShift 15s ease infinite;
                    margin: 0;
                    padding: 20px;
                    min-height: 100vh;
                }}
                
                @keyframes gradientShift {{
                    0% {{ background-position: 0% 50%; }}
                    50% {{ background-position: 100% 50%; }}
                    100% {{ background-position: 0% 50%; }}
                }}
                
                .email-container {{
                    max-width: 650px;
                    margin: 0 auto;
                    background: rgba(255, 255, 255, 0.95);
                    backdrop-filter: blur(20px);
                    border-radius: 24px;
                    overflow: hidden;
                    box-shadow: 
                        0 32px 64px rgba(0, 0, 0, 0.2),
                        0 16px 32px rgba(0, 0, 0, 0.1),
                        inset 0 1px 0 rgba(255, 255, 255, 0.8);
                    animation: fadeInUp 1s ease-out;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                }}
                
                .header {{
                    background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 25%, #EC4899 50%, #F59E0B 75%, #10B981 100%);
                    background-size: 300% 300%;
                    animation: gradientShift 8s ease infinite;
                    padding: 50px 40px;
                    text-align: center;
                    position: relative;
                    overflow: hidden;
                }}
                
                .header::before {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: 
                        radial-gradient(circle at 20% 20%, rgba(255, 255, 255, 0.2) 0%, transparent 50%),
                        radial-gradient(circle at 80% 80%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 40% 40%, rgba(255, 255, 255, 0.05) 0%, transparent 50%);
                }}
                
                .floating-element {{
                    position: absolute;
                    color: rgba(255, 255, 255, 0.6);
                    font-size: 24px;
                    animation: floatingElements 6s ease-in-out infinite;
                    pointer-events: none;
                }}
                
                .floating-element:nth-child(1) {{ top: 15%; left: 10%; animation-delay: 0s; }}
                .floating-element:nth-child(2) {{ top: 25%; right: 15%; animation-delay: 2s; }}
                .floating-element:nth-child(3) {{ bottom: 30%; left: 20%; animation-delay: 4s; }}
                .floating-element:nth-child(4) {{ bottom: 20%; right: 25%; animation-delay: 1s; }}
                .floating-element:nth-child(5) {{ top: 50%; left: 5%; animation-delay: 3s; }}
                
                .logo {{
                    position: relative;
                    z-index: 10;
                    font-family: 'Poppins', sans-serif;
                    font-size: 42px;
                    font-weight: 800;
                    color: white;
                    margin-bottom: 12px;
                    letter-spacing: -1px;
                    background: linear-gradient(45deg, #ffffff, #f8fafc, #ffffff);
                    background-size: 200% auto;
                    -webkit-background-clip: text;
                    background-clip: text;
                    animation: textShimmer 3s linear infinite;
                    text-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
                }}
                
                .tagline {{
                    position: relative;
                    z-index: 10;
                    color: rgba(255, 255, 255, 0.95);
                    font-size: 18px;
                    font-weight: 500;
                    letter-spacing: 0.5px;
                    animation: slideInLeft 1s ease-out 0.3s both;
                }}
                
                .content {{
                    padding: 60px 50px;
                    background: white;
                    position: relative;
                }}
                
                .content::before {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    height: 6px;
                    background: linear-gradient(90deg, #6366F1, #8B5CF6, #EC4899, #F59E0B, #10B981);
                    background-size: 300% 100%;
                    animation: gradientShift 4s ease infinite;
                }}
                
                .verification-badge {{
                    width: 100px;
                    height: 100px;
                    background: linear-gradient(135deg, #6366F1, #8B5CF6);
                    border-radius: 50%;
                    margin: 0 auto 40px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 48px;
                    animation: glowPulse 3s ease-in-out infinite;
                    position: relative;
                }}
                
                .verification-badge::after {{
                    content: '';
                    position: absolute;
                    inset: -8px;
                    border-radius: 50%;
                    background: linear-gradient(45deg, #6366F1, #8B5CF6, #EC4899, #F59E0B);
                    z-index: -1;
                    animation: gradientShift 3s ease infinite;
                    opacity: 0.3;
                }}
                
                .title {{
                    font-family: 'Poppins', sans-serif;
                    color: #1F2937;
                    font-size: 36px;
                    font-weight: 700;
                    text-align: center;
                    margin-bottom: 20px;
                    letter-spacing: -1px;
                    background: linear-gradient(135deg, #1F2937, #4B5563, #6B7280);
                    -webkit-background-clip: text;
                    background-clip: text;
                    animation: slideInRight 1s ease-out 0.5s both;
                }}
                
                .subtitle {{
                    color: #6B7280;
                    font-size: 18px;
                    text-align: center;
                    margin-bottom: 50px;
                    line-height: 1.7;
                    font-weight: 400;
                    animation: fadeInUp 1s ease-out 0.7s both;
                }}
                
                .otp-container {{
                    background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
                    border: 3px solid transparent;
                    background-clip: padding-box;
                    border-radius: 20px;
                    padding: 40px;
                    margin: 50px 0;
                    text-align: center;
                    position: relative;
                    overflow: hidden;
                    animation: bounceIn 0.8s ease-out 1s both;
                }}
                
                .otp-container::before {{
                    content: '';
                    position: absolute;
                    inset: 0;
                    padding: 3px;
                    background: linear-gradient(45deg, #6366F1, #8B5CF6, #EC4899, #F59E0B, #10B981);
                    border-radius: 20px;
                    mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
                    mask-composite: exclude;
                    animation: gradientShift 4s ease infinite;
                }}
                
                .otp-container::after {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    height: 6px;
                    background: linear-gradient(90deg, #6366F1, #8B5CF6, #EC4899);
                    border-radius: 20px 20px 0 0;
                }}
                
                .otp-label {{
                    color: #374151;
                    font-size: 14px;
                    font-weight: 700;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    margin-bottom: 20px;
                    position: relative;
                    z-index: 1;
                }}
                
                .otp-code {{
                    font-size: 48px;
                    font-weight: 800;
                    color: #6366F1;
                    letter-spacing: 12px;
                    font-family: 'Poppins', monospace;
                    margin: 0;
                    text-shadow: 0 4px 20px rgba(99, 102, 241, 0.3);
                    background: linear-gradient(45deg, #6366F1, #8B5CF6);
                    -webkit-background-clip: text;
                    background-clip: text;
                    position: relative;
                    z-index: 1;
                    animation: textShimmer 2s ease infinite;
                }}
                
                .features-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                    gap: 24px;
                    margin: 50px 0;
                }}
                
                .feature-card {{
                    background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
                    padding: 32px 24px;
                    border-radius: 16px;
                    text-align: center;
                    border: 1px solid rgba(99, 102, 241, 0.1);
                    transition: all 0.3s ease;
                    position: relative;
                    overflow: hidden;
                    animation: fadeInUp 0.6s ease-out calc(1.2s + var(--delay, 0s)) both;
                }}
                
                .feature-card:hover {{
                    transform: translateY(-8px);
                    box-shadow: 0 20px 40px rgba(99, 102, 241, 0.15);
                    border-color: rgba(99, 102, 241, 0.3);
                }}
                
                .feature-card::before {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    height: 4px;
                    background: linear-gradient(90deg, #6366F1, #8B5CF6, #EC4899);
                    transform: scaleX(0);
                    transition: transform 0.3s ease;
                }}
                
                .feature-card:hover::before {{
                    transform: scaleX(1);
                }}
                
                .feature-icon {{
                    font-size: 40px;
                    margin-bottom: 16px;
                    animation: bounceIn 0.6s ease-out calc(1.4s + var(--delay, 0s)) both;
                }}
                
                .feature-title {{
                    font-size: 18px;
                    font-weight: 600;
                    color: #374151;
                    margin-bottom: 12px;
                    font-family: 'Poppins', sans-serif;
                }}
                
                .feature-desc {{
                    font-size: 14px;
                    color: #6B7280;
                    line-height: 1.6;
                }}
                
                .cta-section {{
                    text-align: center;
                    margin: 50px 0;
                    animation: fadeInUp 1s ease-out 1.5s both;
                }}
                
                .cta-button {{
                    display: inline-block;
                    background: linear-gradient(135deg, #6366F1, #8B5CF6);
                    color: white;
                    padding: 18px 40px;
                    text-decoration: none;
                    border-radius: 16px;
                    font-weight: 600;
                    font-size: 18px;
                    letter-spacing: 0.5px;
                    transition: all 0.3s ease;
                    box-shadow: 0 8px 30px rgba(99, 102, 241, 0.4);
                    position: relative;
                    overflow: hidden;
                }}
                
                .cta-button::before {{
                    content: '';
                    position: absolute;
                    top: 0;
                    left: -100%;
                    width: 100%;
                    height: 100%;
                    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
                    transition: left 0.5s;
                }}
                
                .cta-button:hover {{
                    transform: translateY(-3px);
                    box-shadow: 0 12px 40px rgba(99, 102, 241, 0.5);
                }}
                
                .cta-button:hover::before {{
                    left: 100%;
                }}
                
                .footer {{
                    background: linear-gradient(135deg, #F9FAFB 0%, #F3F4F6 100%);
                    padding: 40px;
                    text-align: center;
                    border-top: 1px solid #E5E7EB;
                }}
                
                .social-links {{
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    margin-bottom: 24px;
                }}
                
                .social-link {{
                    width: 48px;
                    height: 48px;
                    background: linear-gradient(135deg, #E5E7EB, #D1D5DB);
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    text-decoration: none;
                    color: #6B7280;
                    font-size: 20px;
                    transition: all 0.3s ease;
                }}
                
                .social-link:hover {{
                    background: linear-gradient(135deg, #6366F1, #8B5CF6);
                    color: white;
                    transform: translateY(-3px) scale(1.1);
                }}
                
                .footer-text {{
                    color: #6B7280;
                    font-size: 16px;
                    margin-bottom: 20px;
                    line-height: 1.6;
                }}
                
                .copyright {{
                    color: #9CA3AF;
                    font-size: 13px;
                    margin-top: 20px;
                }}
                
                @media (max-width: 768px) {{
                    body {{ padding: 10px; }}
                    .content {{ padding: 40px 30px; }}
                    .title {{ font-size: 28px; }}
                    .otp-code {{ font-size: 36px; letter-spacing: 8px; }}
                    .features-grid {{ grid-template-columns: 1fr; }}
                    .logo {{ font-size: 32px; }}
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <div class="floating-element">✨</div>
                    <div class="floating-element">💫</div>
                    <div class="floating-element">🌟</div>
                    <div class="floating-element">⭐</div>
                    <div class="floating-element">�</div>
                    
                    <div class="logo">✍️ Blogify</div>
                    <div class="tagline">Where Every Word Matters</div>
                </div>
                
                <div class="content">
                    <div class="verification-badge">🎯</div>
                    
                    <h1 class="title">You're Almost In!</h1>
                    <p class="subtitle">
                        Welcome to Blogify, the platform where creativity meets community! 
                        You're just one step away from joining thousands of passionate writers. 
                        Verify your email to unlock your creative potential.
                    </p>
                    
                    <div class="otp-container">
                        <div class="otp-label">Your Magic Code</div>
                        <div class="otp-code">{otp}</div>
                    </div>
                    
                    <div class="features-grid">
                        <div class="feature-card" style="--delay: 0s;">
                            <div class="feature-icon">🚀</div>
                            <div class="feature-title">Launch Your Voice</div>
                            <div class="feature-desc">Start publishing your thoughts, stories, and ideas with our powerful editor</div>
                        </div>
                        <div class="feature-card" style="--delay: 0.1s;">
                            <div class="feature-icon">🌍</div>
                            <div class="feature-title">Global Community</div>
                            <div class="feature-desc">Connect with readers and writers from around the world</div>
                        </div>
                        <div class="feature-card" style="--delay: 0.2s;">
                            <div class="feature-icon">📊</div>
                            <div class="feature-title">Track Your Impact</div>
                            <div class="feature-desc">See how your content performs with detailed analytics</div>
                        </div>
                        <div class="feature-card" style="--delay: 0.3s;">
                            <div class="feature-icon">💎</div>
                            <div class="feature-title">Premium Tools</div>
                            <div class="feature-desc">Access advanced formatting, SEO tools, and monetization options</div>
                        </div>
                    </div>
                    
                    <div class="cta-section">
                        <a href="#" class="cta-button">Verify & Start Writing</a>
                    </div>
                    
                    <p style="color: #6B7280; font-size: 15px; text-align: center; line-height: 1.7; margin-top: 40px; padding: 20px; background: #F9FAFB; border-radius: 12px; border-left: 4px solid #6366F1;">
                        <strong>Security Note:</strong> This verification code expires in <strong>10 minutes</strong>. 
                        If you didn't create this account, simply ignore this email. Your email is safe with us.
                    </p>
                </div>
                
                <div class="footer">
                    <div class="social-links">
                        <a href="#" class="social-link">📧</a>
                        <a href="#" class="social-link">🐦</a>
                        <a href="#" class="social-link">📘</a>
                        <a href="#" class="social-link">📱</a>
                        <a href="#" class="social-link">💬</a>
                    </div>
                    <p class="footer-text">
                        Have questions? Our community team is here to help!<br>
                        Contact us at <a href="mailto:hello@blogify.com" style="color: #6366F1; text-decoration: none; font-weight: 600;">hello@blogify.com</a>
                    </p>
                    <p class="copyright">
                        © 2025 Blogify. Made with ❤️ for writers everywhere.<br>
                        <a href="#" style="color: #9CA3AF; text-decoration: none;">Privacy</a> • 
                        <a href="#" style="color: #9CA3AF; text-decoration: none;">Terms</a> • 
                        <a href="#" style="color: #9CA3AF; text-decoration: none;">Help</a>
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