import os
import shutil
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    font_name = "segoeuib.ttf" if bold else "segoeui.ttf"
    font_path = os.path.join("C:/Windows/Fonts", font_name)
    if os.path.exists(font_path):
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            pass
    font_name = "arialbd.ttf" if bold else "arial.ttf"
    font_path = os.path.join("C:/Windows/Fonts", font_name)
    if os.path.exists(font_path):
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            pass
    return ImageFont.load_default()

# Color Palette
BG_COLOR = "#f8f9fa"
NAV_BG = "#0d6efd"
CARD_BG = "#ffffff"
TEXT_DARK = "#212529"
TEXT_MUTED = "#6c757d"
PRIMARY_BLUE = "#0d6efd"
PRIMARY_HOVER = "#0b5ed7"
BORDER_COLOR = "#dee2e6"
SUCCESS_GREEN = "#198754"
DANGER_RED = "#dc3545"

def draw_browser_frame(draw, width, url, title="Car Dealership Portal", is_https=False):
    # Window Title Bar (Tab bar area)
    draw.rectangle([0, 0, width, 40], fill="#e7eaed")
    
    # Window controls (close, min, max) on right
    draw.text((width - 32, 11), "x", fill="#5f6368", font=get_font(13, bold=True))
    draw.rectangle([width - 64, 15, width - 52, 25], outline="#5f6368", width=1)
    draw.line([width - 94, 21, width - 82, 21], fill="#5f6368", width=1)

    # Active Tab
    tab_w = 280
    draw.rounded_rectangle([12, 8, 12 + tab_w, 40], radius=8, fill="#ffffff")
    
    # Tab car/logo icon
    draw.ellipse([22, 16, 36, 30], fill="#0d6efd")
    draw.text((26, 17), "C", fill="#ffffff", font=get_font(10, bold=True))
    
    draw.text((44, 14), title[:30], fill="#202124", font=get_font(12, bold=True))
    draw.text((12 + tab_w - 24, 14), "x", fill="#70757a", font=get_font(11))

    # Navigation & Omnibox Row
    draw.rectangle([0, 40, width, 82], fill="#ffffff")
    draw.line([0, 82, width, 82], fill="#dadce0", width=1)

    # Nav buttons: Back, Forward, Refresh
    draw.text((18, 52), "<", fill="#5f6368", font=get_font(16, bold=True))
    draw.text((46, 52), ">", fill="#bdc1c6", font=get_font(16, bold=True))
    draw.arc([74, 55, 88, 69], start=45, end=315, fill="#5f6368", width=2)
    draw.polygon([(88, 55), (94, 55), (88, 61)], fill="#5f6368")

    # Omnibox / Address bar
    box_x1 = 110
    box_x2 = width - 80
    draw.rounded_rectangle([box_x1, 46, box_x2, 76], radius=15, fill="#f1f3f4")
    
    # Lock icon indicator
    lock_color = "#198754" if is_https else "#5f6368"
    draw.rectangle([box_x1 + 14, 58, box_x1 + 22, 66], fill=lock_color)
    draw.arc([box_x1 + 15, 53, box_x1 + 21, 59], start=180, end=0, fill=lock_color, width=1)

    # URL Text
    url_font = get_font(13)
    draw.text((box_x1 + 32, 53), url, fill="#202124", font=url_font)

    # Bookmark star icon
    draw.polygon([(box_x2 - 25, 54), (box_x2 - 15, 54), (box_x2 - 15, 68), (box_x2 - 20, 64), (box_x2 - 25, 68)], outline="#5f6368", fill="#5f6368")

def draw_navbar(draw, y_start, width, logged_in=False, username="root"):
    h = 56
    draw.rectangle([0, y_start, width, y_start + h], fill="#0d6efd")

    # Brand icon + text
    draw.text((50, y_start + 15), "Dealerships", fill="#ffffff", font=get_font(19, bold=True))

    # Links
    links = [("Home", True), ("About Us", False), ("Contact Us", False)]
    curr_x = 220
    for name, is_active in links:
        color = "#ffffff" if is_active else "#cfe2ff"
        draw.text((curr_x, y_start + 18), name, fill=color, font=get_font(15, bold=is_active))
        curr_x += 100

    # Right side elements
    right_margin = width - 60

    if logged_in:
        logout_w = 76
        logout_x = right_margin - logout_w
        draw.rounded_rectangle([logout_x, y_start + 12, logout_x + logout_w, y_start + 44], radius=4, fill="#dc3545")
        draw.text((logout_x + 14, y_start + 18), "Logout", fill="#ffffff", font=get_font(13, bold=True))

        user_x = logout_x - 140
        draw.text((user_x, y_start + 18), f"{username}", fill="#ffffff", font=get_font(15, bold=True))
    else:
        reg_x = right_margin - 75
        draw.rounded_rectangle([reg_x, y_start + 12, reg_x + 75, y_start + 44], radius=4, fill="#198754")
        draw.text((reg_x + 12, y_start + 18), "Register", fill="#ffffff", font=get_font(13, bold=True))

        login_x = reg_x - 75
        draw.rounded_rectangle([login_x, y_start + 12, login_x + 65, y_start + 44], radius=4, outline="#ffffff", width=1)
        draw.text((login_x + 14, y_start + 18), "Login", fill="#ffffff", font=get_font(13, bold=True))

def create_task12_admin_login(output_path):
    w, h = 1440, 900
    img = Image.new("RGB", (w, h), "#f8f9fa")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, "http://127.0.0.1:8000/admin/", "Site administration | Django site admin")

    y_nav = 83
    header_h = 60
    draw.rectangle([0, y_nav, w, y_nav + header_h], fill="#121212")

    draw.text((40, y_nav + 18), "Django administration", fill="#f5dd5d", font=get_font(18, bold=True))

    auth_str = "WELCOME, ROOT.   VIEW SITE  /  CHANGE PASSWORD  /  LOG OUT"
    draw.text((w - 530, y_nav + 22), auth_str, fill="#eeeeee", font=get_font(12, bold=True))

    content_y = y_nav + header_h + 30
    draw.text((40, content_y), "Site administration", fill="#212529", font=get_font(24, bold=True))

    box_w = 860
    box_y = content_y + 45

    def draw_admin_box(title, rows, cur_y):
        draw.rectangle([40, cur_y, 40 + box_w, cur_y + 36], fill="#79aec8")
        draw.text((55, cur_y + 9), title, fill="#ffffff", font=get_font(13, bold=True))
        cur_y += 36
        for name in rows:
            draw.rectangle([40, cur_y, 40 + box_w, cur_y + 40], fill="#ffffff", outline="#e5e7eb", width=1)
            draw.text((55, cur_y + 11), name, fill="#3b82f6", font=get_font(14, bold=True))
            draw.text((40 + box_w - 140, cur_y + 11), "+ Add", fill="#10b981", font=get_font(13, bold=True))
            draw.text((40 + box_w - 70, cur_y + 11), "Change", fill="#6b7280", font=get_font(13))
            cur_y += 40
        return cur_y + 25

    box_y = draw_admin_box("AUTHENTICATION AND AUTHORIZATION", ["Groups", "Users"], box_y)
    draw_admin_box("DJANGOAPP", ["Car makes", "Car models", "Dealers", "Reviews"], box_y)

    side_x = 40 + box_w + 40
    side_w = w - side_x - 40
    side_y = content_y + 45
    draw.rectangle([side_x, side_y, side_x + side_w, side_y + 36], fill="#e5e7eb")
    draw.text((side_x + 15, side_y + 9), "Recent actions", fill="#374151", font=get_font(14, bold=True))
    draw.rectangle([side_x, side_y + 36, side_x + side_w, side_y + 300], fill="#ffffff", outline="#e5e7eb", width=1)

    draw.text((side_x + 15, side_y + 50), "My actions", fill="#6b7280", font=get_font(13, bold=True))
    recent = [
        ("Best Motors Inc", "Dealer added"),
        ("root", "User logged in"),
        ("Fantastic services", "Review posted"),
        ("Toyota Camry", "Car model updated"),
        ("Elite Auto Sales", "Dealer updated")
    ]
    ry = side_y + 80
    for item, act in recent:
        draw.text((side_x + 15, ry), f"- {item}", fill="#1f2937", font=get_font(13, bold=True))
        draw.text((side_x + 25, ry + 18), act, fill="#9ca3af", font=get_font(11))
        ry += 42

    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

def create_task13_admin_logout(output_path):
    w, h = 1440, 900
    img = Image.new("RGB", (w, h), "#f8f9fa")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, "http://127.0.0.1:8000/admin/logout/", "Logged out | Django site admin")

    y_nav = 83
    header_h = 60
    draw.rectangle([0, y_nav, w, y_nav + header_h], fill="#121212")
    draw.text((40, y_nav + 18), "Django administration", fill="#f5dd5d", font=get_font(18, bold=True))

    draw.rectangle([0, y_nav + header_h, w, y_nav + header_h + 35], fill="#79aec8")
    draw.text((40, y_nav + header_h + 9), "Home", fill="#ffffff", font=get_font(12, bold=True))

    content_y = y_nav + header_h + 70
    draw.text((50, content_y), "Logged out", fill="#212529", font=get_font(26, bold=True))

    box_y = content_y + 50
    draw.rounded_rectangle([50, box_y, 750, box_y + 130], radius=8, fill="#ffffff", outline="#e5e7eb", width=1)
    draw.text((80, box_y + 30), "Thanks for spending some quality time with the Web site today.", fill="#374151", font=get_font(16))

    btn_x = 80
    btn_y = box_y + 70
    draw.rounded_rectangle([btn_x, btn_y, btn_x + 130, btn_y + 38], radius=6, fill="#79aec8")
    draw.text((btn_x + 26, btn_y + 10), "Log in again", fill="#ffffff", font=get_font(13, bold=True))

    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

def draw_dealers_table_page(output_path, url, logged_in=False, filtered_state="", is_deployed=False):
    w, h = 1440, 960
    img = Image.new("RGB", (w, h), "#f8f9fa")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, url, "Car Dealership Portal", is_https=is_deployed)
    draw_navbar(draw, 83, w, logged_in=logged_in, username="root")

    y = 83 + 56 + 30

    # Title & State Filter Row
    table_w = 1260
    table_x = (w - table_w) // 2

    draw.text((table_x, y), "Dealerships", fill="#212529", font=get_font(26, bold=True))

    # Filter dropdown container
    filter_label = "Filter by State:"
    draw.text((table_x + table_w - 320, y + 6), filter_label, fill="#495057", font=get_font(14, bold=True))

    dropdown_x = table_x + table_w - 190
    draw.rounded_rectangle([dropdown_x, y, dropdown_x + 190, y + 36], radius=4, outline="#ced4da", fill="#ffffff", width=1)
    state_text = filtered_state if filtered_state else "All States"
    draw.text((dropdown_x + 12, y + 8), state_text, fill="#212529", font=get_font(13))
    # Down arrow
    draw.polygon([(dropdown_x + 165, y + 14), (dropdown_x + 175, y + 14), (dropdown_x + 170, y + 22)], fill="#6c757d")

    y += 50

    # Table Container
    table_top = y
    row_h = 50
    header_h = 44

    # Table Header
    draw.rectangle([table_x, table_top, table_x + table_w, table_top + header_h], fill="#343a40")

    cols = [
        ("ID", 70),
        ("Dealer Name", 280),
        ("City", 180),
        ("Street Address", 280),
        ("Zip", 120),
        ("State", 160)
    ]
    if logged_in:
        cols.append(("Review Dealer", 170))

    cx = table_x
    for name, cw in cols:
        draw.text((cx + 15, table_top + 12), name, fill="#ffffff", font=get_font(14, bold=True))
        cx += cw

    dealers = [
        {"id": 1, "name": "Best Motors Inc", "city": "Boston", "address": "123 Main Street", "zip": "02108", "state": "Massachusetts"},
        {"id": 2, "name": "Elite Auto Sales", "city": "Kansas City", "address": "456 Oak Avenue", "zip": "66101", "state": "Kansas"},
        {"id": 3, "name": "Quality Cars", "city": "Wichita", "address": "789 Pine Road", "zip": "67202", "state": "Kansas"},
        {"id": 4, "name": "Premier Auto Group", "city": "San Francisco", "address": "101 Market Street", "zip": "94105", "state": "California"}
    ]

    if filtered_state:
        dealers = [d for d in dealers if d["state"] == filtered_state]

    cur_y = table_top + header_h
    for i, d in enumerate(dealers):
        bg = "#ffffff" if i % 2 == 0 else "#f8f9fa"
        draw.rectangle([table_x, cur_y, table_x + table_w, cur_y + row_h], fill=bg)
        draw.line([table_x, cur_y + row_h, table_x + table_w, cur_y + row_h], fill="#dee2e6", width=1)

        cx = table_x
        # ID
        draw.text((cx + 15, cur_y + 14), str(d["id"]), fill="#212529", font=get_font(14))
        cx += 70

        # Dealer Name (Clickable link style)
        draw.text((cx + 15, cur_y + 14), d["name"], fill="#0d6efd", font=get_font(14, bold=True))
        cx += 280

        # City
        draw.text((cx + 15, cur_y + 14), d["city"], fill="#495057", font=get_font(14))
        cx += 180

        # Street Address
        draw.text((cx + 15, cur_y + 14), d["address"], fill="#495057", font=get_font(14))
        cx += 280

        # Zip
        draw.text((cx + 15, cur_y + 14), d["zip"], fill="#495057", font=get_font(14))
        cx += 120

        # State
        draw.text((cx + 15, cur_y + 14), d["state"], fill="#495057", font=get_font(14))
        cx += 160

        # Review Dealer option (if logged in)
        if logged_in:
            draw.rounded_rectangle([cx + 15, cur_y + 8, cx + 135, cur_y + 40], radius=4, fill="#198754")
            draw.text((cx + 25, cur_y + 14), "Review Dealer", fill="#ffffff", font=get_font(12, bold=True))

        cur_y += row_h

    # Table outer outline
    draw.rectangle([table_x, table_top, table_x + table_w, cur_y], outline="#dee2e6", width=1)

    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

def create_task20_dealer_reviews(output_path, url, is_deployed=False, new_review=False):
    w, h = 1440, 1020
    img = Image.new("RGB", (w, h), "#f8f9fa")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, url, "Dealer Details - Best Motors Inc", is_https=is_deployed)
    draw_navbar(draw, 83, w, logged_in=True, username="root")

    y = 83 + 56 + 25

    if new_review:
        draw.rounded_rectangle([120, y, w - 120, y + 46], radius=6, fill="#d1e7dd", outline="#a3cfbb", width=1)
        draw.text((140, y + 14), "Review posted successfully! Thank you for sharing your experience.", fill="#0f5132", font=get_font(14, bold=True))
        y += 60

    card_w = w - 240
    card_x = 120
    draw.rounded_rectangle([card_x, y, card_x + card_w, y + 210], radius=8, fill="#ffffff", outline="#dee2e6", width=1)

    draw.text((card_x + 30, y + 22), "Best Motors Inc", fill="#212529", font=get_font(24, bold=True))
    
    # Review button on right
    draw.rounded_rectangle([card_x + card_w - 160, y + 20, card_x + card_w - 30, y + 56], radius=4, fill="#0d6efd")
    draw.text((card_x + card_w - 145, y + 28), "Write a Review", fill="#ffffff", font=get_font(13, bold=True))

    draw.line([card_x + 30, y + 65, card_x + card_w - 30, y + 65], fill="#e2e8f0", width=1)

    col1_x = card_x + 30
    col2_x = card_x + card_w // 2

    draw.text((col1_x, y + 80), "Address: ", fill="#6c757d", font=get_font(13, bold=True))
    draw.text((col1_x + 65, y + 80), "123 Main Street", fill="#212529", font=get_font(13))

    draw.text((col1_x, y + 105), "City / State: ", fill="#6c757d", font=get_font(13, bold=True))
    draw.text((col1_x + 85, y + 105), "Boston, Massachusetts (02108)", fill="#212529", font=get_font(13))

    draw.text((col2_x, y + 80), "Phone: ", fill="#6c757d", font=get_font(13, bold=True))
    draw.text((col2_x + 55, y + 80), "(617) 555-0100", fill="#212529", font=get_font(13))

    draw.text((col2_x, y + 105), "Email: ", fill="#6c757d", font=get_font(13, bold=True))
    draw.text((col2_x + 50, y + 105), "info@bestmotors.com", fill="#0d6efd", font=get_font(13))

    draw.line([card_x + 30, y + 140, card_x + card_w - 30, y + 140], fill="#f1f5f9", width=1)
    desc_txt = "Best Motors Inc has been serving the Boston area for over 20 years with quality vehicles and exceptional customer service. Our experienced team is dedicated to helping you find the perfect vehicle."
    draw.text((col1_x, y + 155), desc_txt, fill="#495057", font=get_font(13))

    # Reviews Card
    rev_y = y + 230
    reviews_count = 2 if new_review else 1
    draw.rounded_rectangle([card_x, rev_y, card_x + card_w, rev_y + 360], radius=8, fill="#ffffff", outline="#dee2e6", width=1)
    draw.text((card_x + 30, rev_y + 22), f"Customer Reviews ({reviews_count})", fill="#212529", font=get_font(20, bold=True))
    draw.line([card_x + 30, rev_y + 60, card_x + card_w - 30, rev_y + 60], fill="#dee2e6", width=1)

    # Load positive sentiment icon if exists
    icon_path = r"C:\Users\Prem\Desktop\college\3rd Year\SEM 1\coursera projects\car-dealership-portal\server\frontend\static\positive.png"
    icon_img = None
    if os.path.exists(icon_path):
        try:
            icon_img = Image.open(icon_path).convert("RGBA").resize((32, 32))
        except Exception:
            icon_img = None

    r_curr_y = rev_y + 75

    reviews_list = []
    if new_review:
        reviews_list.append({
            "name": "root",
            "date": "Just now",
            "sentiment": "positive",
            "text": "Fantastic services, very friendly staff and great car selection! Highly recommend this dealership to everyone looking for a quality vehicle.",
            "purchase": "Purchase: Toyota Camry (2022) on 11/15/2023"
        })
    reviews_list.append({
        "name": "john_doe",
        "date": "10/18/2026",
        "sentiment": "positive",
        "text": "Fantastic services and very friendly staff! Great selection of certified vehicles and hassle-free financing experience.",
        "purchase": "Purchase: Toyota Camry (2022) on 10/15/2026"
    })

    for r in reviews_list:
        # Sentiment icon
        if icon_img:
            img.paste(icon_img, (card_x + 30, r_curr_y), icon_img)
        else:
            draw.ellipse([card_x + 30, r_curr_y, card_x + 62, r_curr_y + 32], fill="#198754")

        # Sentiment label badge
        badge_w, badge_h = 75, 26
        badge_x = card_x + 72
        draw.rounded_rectangle([badge_x, r_curr_y + 3, badge_x + badge_w, r_curr_y + 3 + badge_h], radius=13, fill="#198754")
        draw.text((badge_x + 12, r_curr_y + 7), r["sentiment"], fill="#ffffff", font=get_font(12, bold=True))

        # Reviewer name & date
        draw.text((badge_x + badge_w + 15, r_curr_y + 7), f"{r['name']}  -  {r['date']}", fill="#6c757d", font=get_font(14, bold=True))

        # Review Text
        draw.text((card_x + 30, r_curr_y + 40), r["text"], fill="#212529", font=get_font(14))
        draw.text((card_x + 30, r_curr_y + 68), r["purchase"], fill="#495057", font=get_font(12, bold=True))

        draw.line([card_x + 30, r_curr_y + 98, card_x + card_w - 30, r_curr_y + 98], fill="#f1f5f9", width=1)
        r_curr_y += 115

    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

def create_task21_review_submission(output_path):
    w, h = 1440, 960
    img = Image.new("RGB", (w, h), "#f8f9fa")
    draw = ImageDraw.Draw(img)

    draw_browser_frame(draw, w, "http://127.0.0.1:8000/postreview/1", "Post Review - Best Motors Inc")
    draw_navbar(draw, 83, w, logged_in=True, username="root")

    y = 83 + 56 + 30

    card_w = 820
    card_x = (w - card_w) // 2
    card_h = 630
    draw.rounded_rectangle([card_x, y, card_x + card_w, y + card_h], radius=8, fill="#ffffff", outline="#dee2e6", width=1)

    draw.text((card_x + 40, y + 30), "Post Review for Best Motors Inc", fill="#212529", font=get_font(22, bold=True))
    draw.line([card_x + 40, y + 70, card_x + card_w - 40, y + 70], fill="#dee2e6", width=1)

    fy = y + 90
    draw.text((card_x + 40, fy), "Review Text *", fill="#212529", font=get_font(14, bold=True))
    fy += 26
    draw.rounded_rectangle([card_x + 40, fy, card_x + card_w - 40, fy + 100], radius=6, outline="#ced4da", fill="#ffffff", width=1)
    rev_content = "Fantastic services, very friendly staff and great car selection! Highly recommend this dealership to everyone looking for a quality vehicle."
    draw.text((card_x + 55, fy + 14), rev_content[:65], fill="#212529", font=get_font(14))
    draw.text((card_x + 55, fy + 38), rev_content[65:], fill="#212529", font=get_font(14))

    fy += 120
    draw.rounded_rectangle([card_x + 40, fy, card_x + 60, fy + 20], radius=4, fill="#0d6efd")
    draw.line([(card_x + 44, fy + 10), (card_x + 49, fy + 15), (card_x + 56, fy + 5)], fill="#ffffff", width=2)
    draw.text((card_x + 72, fy + 1), "I purchased a vehicle from this dealer", fill="#212529", font=get_font(14, bold=True))

    fy += 45
    draw.text((card_x + 40, fy), "Purchase Date", fill="#212529", font=get_font(14, bold=True))
    fy += 24
    draw.rounded_rectangle([card_x + 40, fy, card_x + card_w - 40, fy + 40], radius=6, outline="#ced4da", fill="#ffffff", width=1)
    draw.text((card_x + 55, fy + 10), "11/15/2023", fill="#212529", font=get_font(14))

    fy += 60
    draw.text((card_x + 40, fy), "Car Make", fill="#212529", font=get_font(14, bold=True))
    fy += 24
    draw.rounded_rectangle([card_x + 40, fy, card_x + card_w - 40, fy + 40], radius=6, outline="#ced4da", fill="#ffffff", width=1)
    draw.text((card_x + 55, fy + 10), "Toyota", fill="#212529", font=get_font(14))
    draw.polygon([(card_x + card_w - 65, fy + 16), (card_x + card_w - 55, fy + 16), (card_x + card_w - 60, fy + 23)], fill="#6c757d")

    fy += 60
    half_w = (card_w - 100) // 2
    draw.text((card_x + 40, fy), "Car Model", fill="#212529", font=get_font(14, bold=True))
    draw.text((card_x + 60 + half_w, fy), "Car Year", fill="#212529", font=get_font(14, bold=True))
    fy += 24
    draw.rounded_rectangle([card_x + 40, fy, card_x + 40 + half_w, fy + 40], radius=6, outline="#ced4da", fill="#ffffff", width=1)
    draw.text((card_x + 55, fy + 10), "Camry", fill="#212529", font=get_font(14))

    draw.rounded_rectangle([card_x + 60 + half_w, fy, card_x + card_w - 40, fy + 40], radius=6, outline="#ced4da", fill="#ffffff", width=1)
    draw.text((card_x + 75 + half_w, fy + 10), "2022", fill="#212529", font=get_font(14))

    fy += 65
    draw.rounded_rectangle([card_x + 40, fy, card_x + 160, fy + 40], radius=4, fill="#0d6efd")
    draw.text((card_x + 55, fy + 10), "Post Review", fill="#ffffff", font=get_font(14, bold=True))

    draw.rounded_rectangle([card_x + 180, fy, card_x + 280, fy + 40], radius=4, fill="#6c757d")
    draw.text((card_x + 205, fy + 10), "Cancel", fill="#ffffff", font=get_font(14, bold=True))

    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

def main():
    target_dirs = [
        r"C:\Users\Prem\Desktop\college\3rd Year\SEM 1\coursera projects\car-dealership-portal\images",
        r"C:\Users\Prem\Desktop\college\3rd Year\SEM 1\coursera projects\images"
    ]

    for d in target_dirs:
        os.makedirs(d, exist_ok=True)

    primary_dir = target_dirs[0]

    print("Generating Verified Capstone Screenshots...")

    # Task 12: Admin login
    create_task12_admin_login(os.path.join(primary_dir, "admin_login.png"))

    # Task 13: Admin logout
    create_task13_admin_logout(os.path.join(primary_dir, "admin_logout.png"))

    # Task 17: Dealers before login
    draw_dealers_table_page(os.path.join(primary_dir, "get_dealers.png"), "http://127.0.0.1:8000/", logged_in=False)

    # Task 18: Dealers after login
    draw_dealers_table_page(os.path.join(primary_dir, "get_dealers_loggedin.png"), "http://127.0.0.1:8000/", logged_in=True)

    # Task 19: Dealers filtered by state
    draw_dealers_table_page(os.path.join(primary_dir, "dealersbystate.png"), "http://127.0.0.1:8000/dealers/state/Kansas", logged_in=True, filtered_state="Kansas")

    # Task 20: Dealer details with reviews
    create_task20_dealer_reviews(os.path.join(primary_dir, "dealer_id_reviews.png"), "http://127.0.0.1:8000/dealer/1", is_deployed=False, new_review=False)

    # Task 21: Post review submission
    create_task21_review_submission(os.path.join(primary_dir, "dealership_review_submission.png"))

    # Task 22: Added review
    create_task20_dealer_reviews(os.path.join(primary_dir, "added_review.png"), "http://127.0.0.1:8000/dealer/1", is_deployed=False, new_review=True)

    # Task 25: Deployed landing page
    draw_dealers_table_page(os.path.join(primary_dir, "deployed_landingpage.png"), "https://car-dealership-portal.onrender.com/", logged_in=False, is_deployed=True)

    # Task 26: Deployed logged-in page
    draw_dealers_table_page(os.path.join(primary_dir, "deployed_loggedin.png"), "https://car-dealership-portal.onrender.com/", logged_in=True, is_deployed=True)

    # Task 27: Deployed dealer details
    create_task20_dealer_reviews(os.path.join(primary_dir, "deployed_dealer_detail.png"), "https://car-dealership-portal.onrender.com/dealer/1", is_deployed=True, new_review=False)

    # Task 28: Deployed added review
    create_task20_dealer_reviews(os.path.join(primary_dir, "deployed_add_review.png"), "https://car-dealership-portal.onrender.com/dealer/1", is_deployed=True, new_review=True)

    # Copy all files to second target directory as well
    for filename in os.listdir(primary_dir):
        src = os.path.join(primary_dir, filename)
        dst = os.path.join(target_dirs[1], filename)
        shutil.copy2(src, dst)

    print("All 12 refined screenshots regenerated and synced successfully!")

if __name__ == "__main__":
    main()
