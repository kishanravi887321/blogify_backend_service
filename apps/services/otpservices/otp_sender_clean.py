from .base_otp import BaseOtpEmailSender

class LoginOtpSender(BaseOtpEmailSender):
    def __init__(self, email):
        super().__init__(email, purpose="login")

    def send(self):
        otp = self.generate_otp()
        subject = "âœï¸ Blogify - Secure Login Verification"
        
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
                    <div class="logo">âœï¸ Blogify</div>
                    <div class="tagline">Where Stories Come to Life</div>
                </div>
                
                <div class="content">
                    <div class="security-icon">ðŸ”</div>
                    
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
                            ðŸ›¡ï¸ Security Best Practices
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
                        Â© 2025 Blogify. All rights reserved. | 
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
        â€¢ Never share this code with anyone
        â€¢ If you didn't request this login, secure your account immediately
        â€¢ Contact support@blogify.com if you need assistance
        
        Happy blogging!
        The Blogify Team
        
        ---
        Â© 2025 Blogify. All rights reserved.
        """

        self.send_email(subject, text_content, html_content=html_content)
        return otp


class ForgetPasswordOtpSender(BaseOtpEmailSender):
    def __init__(self, email):
        super().__init__(email, purpose="forget")

    def send(self):
        otp = self.generate_otp()
        subject = "ðŸ”‘ Blogify - Password Reset Verification"
        
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
                    <div class="logo">ðŸ”‘ Blogify</div>
                    <div class="tagline">Password Recovery Service</div>
                </div>
                
                <div class="content">
                    <div class="reset-icon">ðŸ”“</div>
                    
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
                            âš ï¸ Important Security Notice
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
                        Â© 2025 Blogify. All rights reserved.
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
        â€¢ This code expires in 10 minutes
        â€¢ If you didn't request this reset, contact support immediately
        â€¢ The code can only be used once for your protection
        
        Need help? Contact support@blogify.com
        
        ---
        Â© 2025 Blogify. All rights reserved.
        """

        self.send_email(subject, text_content, html_content=html_content)
        return otp


class WelcomeEmailSender(BaseOtpEmailSender):
    def __init__(self, email, username=None):
        super().__init__(email, purpose="welcome")
        self.username = username or email

    def send(self):
        subject = "ðŸŽ‰ Welcome to Blogify - Your Writing Journey Begins!"
        
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
                    <div class="logo">âœï¸ Blogify</div>
                    <div class="welcome-text">Welcome to the Community!</div>
                </div>
                
                <div class="content">
                    <h1 class="greeting">Hello {self.username}! ðŸ‘‹</h1>
                    <p class="intro-text">
                        Welcome to Blogify, where your stories come to life! We're thrilled to have you join our 
                        community of passionate writers, creators, and storytellers. Your writing journey starts now!
                    </p>
                    
                    <div class="feature-grid">
                        <div class="feature-card">
                            <div class="feature-icon">âœï¸</div>
                            <div class="feature-title">Rich Editor</div>
                            <div class="feature-desc">Create beautiful posts with our intuitive writing tools</div>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">ðŸŒ</div>
                            <div class="feature-title">Global Reach</div>
                            <div class="feature-desc">Share your stories with readers worldwide</div>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">ðŸ“ˆ</div>
                            <div class="feature-title">Analytics</div>
                            <div class="feature-desc">Track your content performance and engagement</div>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">ðŸ‘¥</div>
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
                        Â© 2025 Blogify. All rights reserved.
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
        â€¢ Create beautiful posts with our rich editor
        â€¢ Share your stories with readers worldwide  
        â€¢ Track your content performance
        â€¢ Connect with fellow writers
        
        Ready to start writing? Visit your dashboard and create your first post!
        
        Questions? Contact us at support@blogify.com
        
        Happy writing!
        The Blogify Team
        
        ---
        Â© 2025 Blogify. All rights reserved.
        """

        self.send_email(subject, text_content, html_content=html_content)
        return "Welcome email sent successfully!"


class RegistrationOtpSender(BaseOtpEmailSender):
    def __init__(self, email):
        super().__init__(email, purpose="register")

    def send(self):
        otp = self.generate_otp()
        subject = "✨ Welcome to Blogify - Verify Your Account!"
        
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Blogify</title>
            <!--[if mso]>
            <noscript>
                <xml>
                    <o:OfficeDocumentSettings>
                        <o:PixelsPerInch>96</o:PixelsPerInch>
                    </o:OfficeDocumentSettings>
                </xml>
            </noscript>
            <![endif]-->
        </head>
        <body style="margin: 0; padding: 0; background-color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
            <table cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #f8fafc; padding: 40px 0;">
                <tr>
                    <td align="center">
                        <table cellpadding="0" cellspacing="0" border="0" width="600" style="max-width: 600px; background-color: #ffffff; border-radius: 16px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1); overflow: hidden;">
                            
                            <!-- Header -->
                            <tr>
                                <td style="background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%); padding: 50px 40px; text-align: center;">
                                    <h1 style="margin: 0; color: #ffffff; font-size: 32px; font-weight: 700; letter-spacing: -0.5px;">
                                        ✍️ Blogify
                                    </h1>
                                    <p style="margin: 8px 0 0 0; color: rgba(255, 255, 255, 0.9); font-size: 16px; font-weight: 500;">
                                        Where Every Word Matters
                                    </p>
                                </td>
                            </tr>
                            
                            <!-- Content -->
                            <tr>
                                <td style="padding: 50px 40px;">
                                    
                                    <!-- Verification Icon -->
                                    <table cellpadding="0" cellspacing="0" border="0" width="100%">
                                        <tr>
                                            <td align="center" style="padding-bottom: 30px;">
                                                <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #6366f1, #8b5cf6); border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 36px; color: white;">
                                                    🎯
                                                </div>
                                            </td>
                                        </tr>
                                    </table>
                                    
                                    <!-- Main Title -->
                                    <h2 style="margin: 0 0 20px 0; color: #1f2937; font-size: 28px; font-weight: 700; text-align: center; letter-spacing: -0.5px;">
                                        You're Almost In!
                                    </h2>
                                    
                                    <!-- Subtitle -->
                                    <p style="margin: 0 0 40px 0; color: #6b7280; font-size: 16px; line-height: 1.6; text-align: center;">
                                        Welcome to Blogify, the platform where creativity meets community! 
                                        You're just one step away from joining thousands of passionate writers. 
                                        Verify your email to unlock your creative potential.
                                    </p>
                                    
                                    <!-- OTP Container -->
                                    <table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin: 40px 0;">
                                        <tr>
                                            <td align="center">
                                                <table cellpadding="0" cellspacing="0" border="0" style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); border: 2px solid #e2e8f0; border-radius: 12px; padding: 30px;">
                                                    <tr>
                                                        <td align="center">
                                                            <p style="margin: 0 0 15px 0; color: #374151; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                                                                Your Verification Code
                                                            </p>
                                                            <div style="font-size: 36px; font-weight: 700; color: #6366f1; letter-spacing: 6px; font-family: monospace; margin: 0; text-align: center;">
                                                                {otp}
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                    
                                    <!-- Features Section -->
                                    <table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin: 40px 0;">
                                        <tr>
                                            <td style="padding: 20px 0;">
                                                <h3 style="margin: 0 0 20px 0; color: #1f2937; font-size: 20px; font-weight: 600; text-align: center;">
                                                    🚀 What awaits you in Blogify:
                                                </h3>
                                                
                                                <!-- Feature Items -->
                                                <table cellpadding="0" cellspacing="0" border="0" width="100%">
                                                    <tr>
                                                        <td style="padding: 8px 0; color: #374151; font-size: 15px; line-height: 1.6;">
                                                            ✍️ <strong>Powerful Editor:</strong> Write with our intuitive, feature-rich editor
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 8px 0; color: #374151; font-size: 15px; line-height: 1.6;">
                                                            🌐 <strong>Global Audience:</strong> Reach readers from around the world
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 8px 0; color: #374151; font-size: 15px; line-height: 1.6;">
                                                            📊 <strong>Analytics Dashboard:</strong> Track your content's performance
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 8px 0; color: #374151; font-size: 15px; line-height: 1.6;">
                                                            👥 <strong>Writer Community:</strong> Connect with fellow creators
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 8px 0; color: #374151; font-size: 15px; line-height: 1.6;">
                                                            🎨 <strong>Customization:</strong> Personalize your author profile
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                    
                                    <!-- CTA Button -->
                                    <table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin: 40px 0;">
                                        <tr>
                                            <td align="center">
                                                <a href="#" style="display: inline-block; background: linear-gradient(135deg, #6366f1, #8b5cf6); color: #ffffff; text-decoration: none; padding: 16px 32px; border-radius: 12px; font-weight: 600; font-size: 16px; letter-spacing: 0.5px;">
                                                    Verify & Start Writing
                                                </a>
                                            </td>
                                        </tr>
                                    </table>
                                    
                                    <!-- Security Note -->
                                    <table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin: 30px 0;">
                                        <tr>
                                            <td style="background: #f9fafb; border-left: 4px solid #6366f1; border-radius: 8px; padding: 20px;">
                                                <p style="margin: 0; color: #6b7280; font-size: 14px; line-height: 1.6;">
                                                    <strong style="color: #374151;">🔒 Security Note:</strong> This verification code expires in <strong>10 minutes</strong>. 
                                                    If you didn't create this account, simply ignore this email. Your email is safe with us.
                                                </p>
                                            </td>
                                        </tr>
                                    </table>
                                    
                                </td>
                            </tr>
                            
                            <!-- Footer -->
                            <tr>
                                <td style="background: #f9fafb; padding: 30px 40px; text-align: center; border-top: 1px solid #e5e7eb;">
                                    
                                    <!-- Social Links -->
                                    <table cellpadding="0" cellspacing="0" border="0" width="100%">
                                        <tr>
                                            <td align="center" style="padding-bottom: 20px;">
                                                <a href="#" style="display: inline-block; margin: 0 8px; width: 36px; height: 36px; background: #e5e7eb; border-radius: 50%; text-decoration: none; line-height: 36px; color: #6b7280; font-size: 16px;">📧</a>
                                                <a href="#" style="display: inline-block; margin: 0 8px; width: 36px; height: 36px; background: #e5e7eb; border-radius: 50%; text-decoration: none; line-height: 36px; color: #6b7280; font-size: 16px;">🐦</a>
                                                <a href="#" style="display: inline-block; margin: 0 8px; width: 36px; height: 36px; background: #e5e7eb; border-radius: 50%; text-decoration: none; line-height: 36px; color: #6b7280; font-size: 16px;">📘</a>
                                                <a href="#" style="display: inline-block; margin: 0 8px; width: 36px; height: 36px; background: #e5e7eb; border-radius: 50%; text-decoration: none; line-height: 36px; color: #6b7280; font-size: 16px;">📱</a>
                                            </td>
                                        </tr>
                                    </table>
                                    
                                    <p style="margin: 0 0 15px 0; color: #6b7280; font-size: 14px; line-height: 1.6;">
                                        Have questions? Our community team is here to help!<br>
                                        Contact us at <a href="mailto:hello@blogify.com" style="color: #6366f1; text-decoration: none; font-weight: 600;">hello@blogify.com</a>
                                    </p>
                                    
                                    <p style="margin: 0; color: #9ca3af; font-size: 12px;">
                                        © 2025 Blogify. Made with ❤️ for writers everywhere.<br>
                                        <a href="#" style="color: #9ca3af; text-decoration: none;">Privacy</a> • 
                                        <a href="#" style="color: #9ca3af; text-decoration: none;">Terms</a> • 
                                        <a href="#" style="color: #9ca3af; text-decoration: none;">Help</a>
                                    </p>
                                </td>
                            </tr>
                            
                        </table>
                    </td>
                </tr>
            </table>
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
