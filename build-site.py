#!/usr/bin/env python3
"""Build wrangliator.com — pure editorial backlink site for Bartact Wrangler/Gladiator products."""

import os

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

NAV = """<nav>
<a href="/">Home</a>
<a href="/jeep-wrangler-seat-covers.html">Seat Covers</a>
<a href="/paracord-grab-handles.html">Grab Handles</a>
<a href="/molle-accessories.html">MOLLE</a>
<a href="/door-storage-bags.html">Door Bags</a>
<a href="/fire-extinguisher-mount.html">Fire Ext. Mount</a>
<a href="/sun-shades.html">Sun Shades</a>
<a href="/suspension-limit-straps.html">Limit Straps</a>
<a href="/console-organizers.html">Console</a>
<a href="/550-paracord.html">550 Paracord</a>
</nav>"""

CSS = """<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:#1a1a1a;line-height:1.7;background:#fff}
header{background:#1a1a2e;color:#fff;padding:16px 20px;display:flex;align-items:center;gap:20px;flex-wrap:wrap}
header a.logo{color:#daa520;font-size:22px;font-weight:800;text-decoration:none;letter-spacing:1px}
nav{display:flex;flex-wrap:wrap;gap:8px}
nav a{color:#ccc;text-decoration:none;font-size:13px;padding:4px 10px;border-radius:4px;transition:background .2s}
nav a:hover{background:rgba(255,255,255,.1);color:#fff}
.hero{background:linear-gradient(135deg,#1a1a2e,#2d2d4e);color:#fff;padding:60px 20px;text-align:center}
.hero h1{font-size:clamp(24px,4vw,42px);font-weight:800;margin-bottom:16px;line-height:1.2}
.hero p{font-size:18px;color:#ccc;max-width:640px;margin:0 auto}
.container{max-width:860px;margin:0 auto;padding:40px 20px}
h2{font-size:24px;font-weight:700;margin:32px 0 12px;color:#1a1a2e}
h3{font-size:18px;font-weight:700;margin:24px 0 8px;color:#333}
p{margin-bottom:16px}
a{color:#c8860a;text-decoration:none}
a:hover{text-decoration:underline}
.bartact-link{background:#1f1c0a;border:1px solid #daa520;border-radius:6px;padding:14px 18px;margin:24px 0;display:block}
.bartact-link span{color:#daa520;font-weight:700}
.vehicle-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;margin:24px 0}
.vehicle-card{background:#f7f7f7;border-radius:8px;padding:18px;border-left:3px solid #daa520}
.vehicle-card h4{font-weight:700;margin-bottom:6px;font-size:14px}
.vehicle-card p{font-size:13px;color:#555;margin:0}
ul{margin:12px 0 16px 20px}
ul li{margin-bottom:6px}
footer{background:#1a1a2e;color:#888;text-align:center;padding:24px;font-size:13px;margin-top:60px}
footer a{color:#aaa}
@media(max-width:600px){.vehicle-grid{grid-template-columns:1fr}}
</style>"""

def page(title, meta_desc, slug, content, canonical=None):
    can = canonical or f"https://wrangliator.com/{slug}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Wrangliator</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{can}">
{CSS}
</head>
<body>
<header>
<a class="logo" href="/">WRANGLIATOR</a>
{NAV}
</header>
{content}
<footer><p>Wrangliator — Jeep Wrangler &amp; Gladiator product guides. All products made in the USA by <a href="https://bartact.com" rel="noopener">Bartact</a>.</p></footer>
</body>
</html>"""

PAGES = {}

# ── HOMEPAGE ───────────────────────────────────────────────────────────────────
PAGES["index.html"] = page(
    "Wrangliator — Jeep Wrangler & Gladiator Product Guides",
    "Wrangliator covers every Bartact-built accessory for Jeep Wrangler and Gladiator: seat covers, grab handles, MOLLE gear, door bags, limit straps, and more. Made in Temecula, CA.",
    "",
    """<div class="hero">
<h1>Built for Wrangler.<br>Built for Gladiator.</h1>
<p>Guides for every Bartact-made accessory — seat covers, paracord grab handles, MOLLE systems, and more. All USA-made, all Jeep-specific.</p>
</div>
<div class="container">
<p>The Jeep Wrangler and Gladiator aftermarket is enormous and often overwhelming. Wrangliator exists to cut through the noise on one specific category: the accessories that <a href="https://bartact.com" rel="noopener">Bartact</a> manufactures in Temecula, California, specifically for Wrangler and Gladiator owners.</p>
<p>These aren't generic truck accessories. They're cut, sewn, and quality-checked for specific Wrangler and Gladiator platforms — JKU and JK, JLU and JL, the JT Gladiator, and legacy TJ and LJ platforms going back to 1997. Every product guide on this site covers fitment by generation, what the product actually does, and where to buy directly from Bartact.</p>
<h2>What We Cover</h2>
<div class="vehicle-grid">
<div class="vehicle-card"><h4>Seat Covers</h4><p>Custom-fit for JKU/JK, JLU/JL, JT Gladiator, and TJ/LJ. MOLLE-equipped tactical options available.</p></div>
<div class="vehicle-card"><h4>Paracord Grab Handles</h4><p>USA-sourced 550 paracord. Roll bar-mounted for JKU, JLU, and Gladiator.</p></div>
<div class="vehicle-card"><h4>MOLLE Accessories</h4><p>Panels, buckles, clips, and pouches. Mil-spec PALS webbing compatible.</p></div>
<div class="vehicle-card"><h4>Door Storage Bags</h4><p>Wrangliator door bags for JL/JLU. Maximize door pocket utility.</p></div>
<div class="vehicle-card"><h4>Fire Extinguisher Mounts</h4><p>Roll bar-mounted extinguisher holders. JK, JL, and Gladiator fitment.</p></div>
<div class="vehicle-card"><h4>Sun Shades</h4><p>Tactical sun shades for JK/JKU, JL/JLU, and Gladiator. Blocks heat, fits over doors.</p></div>
<div class="vehicle-card"><h4>Suspension Limit Straps</h4><p>Protect your suspension at full droop. Adjustable, heavy-duty, USA-made.</p></div>
<div class="vehicle-card"><h4>Console Organizers</h4><p>Console and storage solutions for Wrangler and Gladiator interiors.</p></div>
<div class="vehicle-card"><h4>550 Paracord</h4><p>USA-sourced military-spec 550 paracord. The material behind Bartact's grab handles.</p></div>
</div>
<h2>Why Bartact</h2>
<p>Bartact has been building Wrangler-specific accessories in Temecula, California since before MOLLE seat backs were a production Jeep option. The entire product line is designed around the specific seat shapes, roll bar diameters, and fitment requirements of the Wrangler and Gladiator platforms. Nothing here is a universal fit stretched to work — it's cut for your Jeep.</p>
<p>Every guide on this site links directly to the corresponding <a href="https://bartact.com" rel="noopener">Bartact</a> collection or product page, so you can read here and buy there.</p>
<a class="bartact-link" href="https://bartact.com" rel="noopener"><span>Shop all Bartact products →</span> Made in Temecula, CA. Custom-fit for your Wrangler or Gladiator.</a>
</div>""",
    "https://wrangliator.com/"
)

# ── SEAT COVERS ────────────────────────────────────────────────────────────────
PAGES["jeep-wrangler-seat-covers.html"] = page(
    "Jeep Wrangler Seat Covers — JKU, JLU, JK, JL, Gladiator | Wrangliator",
    "Guide to Bartact seat covers for Jeep Wrangler JKU/JK and JLU/JL, Gladiator JT, and TJ/LJ. Custom-fit tactical seat covers made in Temecula, CA.",
    "jeep-wrangler-seat-covers.html",
    """<div class="hero">
<h1>Jeep Wrangler Seat Covers</h1>
<p>Custom-fit for JKU/JK, JLU/JL, Gladiator JT, and TJ/LJ. Made in Temecula, CA.</p>
</div>
<div class="container">
<p>A seat cover for a Jeep Wrangler isn't the same as a seat cover for a truck or an SUV. The Wrangler gets rained on through the top, mudded through open doors, and worked harder than almost any vehicle on the road. A cover that doesn't account for the specific seat shape, headrest configuration, and side airbag placement of each generation is going to fit badly, look worse, and fail faster.</p>
<p>Bartact's <a href="https://bartact.com/collections/seat-covers" rel="noopener">Jeep Wrangler seat covers</a> are patterned specifically for each Wrangler generation and trim level. They're cut, sewn, and quality-checked in Temecula, California. No universal fits. No overseas sourcing of the finished product.</p>

<h2>Fitment by Generation</h2>

<h3>JKU and JK Wrangler (2007–2018)</h3>
<p>The JK generation ran from 2007 to 2018 and was the best-selling Wrangler in history, which means the aftermarket for it is mature and specific. Bartact patterns their <a href="https://bartact.com/collections/jeep-wrangler-jk-jku-seat-covers" rel="noopener">JKU and JK seat covers</a> separately for front buckets and rear benches, accounting for the differences between two-door JK and four-door JKU rear seat configurations. The JKU leads in Bartact's lineup because four-door demand is higher — if you're ordering for a two-door JK, confirm that in the product options.</p>
<p>Important JK fitment note: Jeep made running changes to the JK seat design across the production run, including headrest stalk diameter differences between early and late production. Bartact accounts for these variations — check the product page for year-specific fitment guidance before ordering.</p>

<h3>JLU and JL Wrangler (2018–Present)</h3>
<p>The JL platform introduced side-mounted seat airbags as standard or optional equipment depending on trim. Any seat cover installed on an airbag-equipped JL needs properly designed seam placement to allow the airbag to deploy correctly. Bartact's <a href="https://bartact.com/collections/jeep-wrangler-jl-jlu-seat-covers" rel="noopener">JLU and JL seat covers</a> are designed with this in mind — the airbag seam is not permanently sewn over.</p>
<p>The JLU (four-door) is the more common configuration and leads in Bartact's product lineup. JL two-door owners should confirm two-door rear fitment when ordering rear covers, as the seat configuration differs from the JLU.</p>

<h3>Gladiator JT (2020–Present)</h3>
<p>The Gladiator shares its front seat design with the JL platform, which means JL-spec front covers generally fit the JT as well. Rear seating is a different story — the Gladiator JT has a truck-style rear bench that's unique to the platform. Bartact's <a href="https://bartact.com/collections/jeep-gladiator-jt-seat-covers" rel="noopener">Gladiator JT seat covers</a> account for this rear seat difference specifically.</p>

<h3>TJ and LJ Wrangler (1997–2006)</h3>
<p>The TJ and LJ (Unlimited) platforms predate modern side airbag requirements, which simplifies cover fitment in one sense — there's no airbag seam to navigate. However, the seat shapes and headrest configurations of the TJ era are distinct from the JK and JL platforms, so platform-specific patterning still matters. Bartact makes seat covers for TJ and LJ owners who want the same quality and fitment approach applied to the earlier platform.</p>

<h2>MOLLE Seat Backs</h2>
<p>One of the features that distinguishes Bartact's Wrangler seat covers is the availability of MOLLE/PALS webbing on the seat backs. MOLLE webbing allows you to attach pouches, organizers, hydration carriers, and other gear directly to the back of the front seats — useful for trail gear, recovery kit components, and day-to-day organization. The webbing is load-rated, not decorative. For more on the MOLLE system, see the <a href="/molle-accessories.html">MOLLE accessories guide</a>.</p>

<h2>Made in Temecula, CA</h2>
<p>Every Bartact seat cover is cut and sewn at the Temecula, California facility. Manufacturing in-house means Bartact controls quality at every step — material selection, pattern accuracy, stitching consistency, and final inspection. When something's not right, you're dealing with the manufacturer, not a third-party distributor.</p>

<a class="bartact-link" href="https://bartact.com/collections/seat-covers" rel="noopener"><span>Browse all Bartact seat covers →</span> Custom-fit for every Wrangler and Gladiator generation.</a>
</div>"""
)

# ── PARACORD GRAB HANDLES ──────────────────────────────────────────────────────
PAGES["paracord-grab-handles.html"] = page(
    "Paracord Grab Handles for Jeep Wrangler & Gladiator | Wrangliator",
    "Bartact paracord grab handles for Jeep Wrangler JKU/JK, JLU/JL, and Gladiator JT. USA-sourced 550 paracord, roll bar mounted, made in Temecula, CA.",
    "paracord-grab-handles.html",
    """<div class="hero">
<h1>Paracord Grab Handles</h1>
<p>550 paracord. Roll bar mounted. JKU/JK, JLU/JL, and Gladiator JT. USA-sourced and made in Temecula, CA.</p>
</div>
<div class="container">
<p>A grab handle on a Wrangler's roll bar sounds like a simple thing — something to hold onto when the trail gets rough. Bartact's <a href="https://bartact.com/collections/grab-handles-for-jeep-wrangler-gladiator-ford-bronco-utvs-buggies-rails" rel="noopener">paracord grab handles</a> are that, but the material choice is what makes them stand apart from fabric or neoprene alternatives. USA-sourced 550 paracord is the same cord used in military and outdoor survival applications — it's rated for load, it handles UV exposure, and it develops a natural patina with use rather than degrading or cracking the way coated materials tend to.</p>

<h2>What 550 Paracord Means</h2>
<p>"550" refers to the minimum breaking strength of the paracord in pounds — 550 lbs. The construction is a braided outer sheath around seven inner strands, each of which can be removed for use independently. The material is UV-resistant, water-resistant, and maintains its strength and flexibility across a wide temperature range. For a grab handle application, it's the right choice — strong, lightweight, and durable in the conditions a Wrangler actually operates in.</p>
<p>Bartact sources its paracord in the USA. For more on the material itself, see the <a href="/550-paracord.html">550 paracord guide</a>.</p>

<h2>Fitment by Platform</h2>

<h3>JKU and JK Wrangler (2007–2018)</h3>
<p>The JK roll bar diameter is consistent across the production run, which makes grab handle fitment relatively straightforward. Bartact's handles mount directly to the factory roll bar — the paracord loop wraps around the bar and secures with a hook-and-loop closure reinforced by a retention strap. No drilling. No permanent modification. Installation takes a few minutes and removal is equally fast for topless driving days.</p>
<p>The JKU (four-door) has more roll bar positions available for handle placement than the two-door JK, and is the more common configuration in Bartact's lineup. If you're ordering for a two-door JK, confirm the roll bar position in the product options.</p>

<h3>JLU and JL Wrangler (2018–Present)</h3>
<p>The JL platform roll bar is dimensionally similar to the JK, and Bartact's grab handle mounting approach is consistent across both generations. The paracord loop slides over the roll bar and locks in place — same installation, same removal speed.</p>
<p>JLU (four-door) is the lead configuration. JL two-door owners have fewer roll bar mounting positions but the handles themselves are the same product.</p>

<h3>Gladiator JT (2020–Present)</h3>
<p>The Gladiator shares its roll bar architecture with the JL platform, and Bartact's paracord grab handles fit the JT roll bar positions accordingly. The Gladiator's longer wheelbase and cab configuration don't affect grab handle fitment — the roll bar diameter and mounting approach are the same.</p>

<h2>Color Options</h2>
<p>Bartact offers paracord grab handles in multiple colorways that coordinate with the seat cover lineup. If you're building out a complete interior, handles and seat covers in matching colors are available — see the full range at <a href="https://bartact.com/collections/grab-handles-for-jeep-wrangler-gladiator-ford-bronco-utvs-buggies-rails" rel="noopener">Bartact's grab handle collection</a>.</p>

<h2>Made in Temecula, CA</h2>
<p>Like everything Bartact makes, the paracord grab handles are manufactured in Temecula, California. The paracord is USA-sourced and the assembly — wrapping, stitching the ends, attaching the closure hardware — is done in-house. That's the whole supply chain from material to finished product.</p>

<a class="bartact-link" href="https://bartact.com/collections/grab-handles-for-jeep-wrangler-gladiator-ford-bronco-utvs-buggies-rails" rel="noopener"><span>Shop Bartact paracord grab handles →</span> JKU, JLU, JK, JL, Gladiator. USA-sourced 550 paracord.</a>
</div>"""
)

# ── MOLLE ACCESSORIES ──────────────────────────────────────────────────────────
PAGES["molle-accessories.html"] = page(
    "MOLLE Accessories for Jeep Wrangler & Gladiator | Wrangliator",
    "Bartact MOLLE accessories for Jeep Wrangler and Gladiator — panels, pouches, buckles, and clips. Mil-spec PALS webbing compatible. Made in Temecula, CA.",
    "molle-accessories.html",
    """<div class="hero">
<h1>MOLLE Accessories</h1>
<p>Panels, pouches, buckles, and clips for Jeep Wrangler and Gladiator. PALS webbing compatible.</p>
</div>
<div class="container">
<p>MOLLE stands for Modular Lightweight Load-carrying Equipment. It's a system originally developed for military use that uses a grid of webbing loops — called PALS webbing (Pouch Attachment Ladder System) — to allow pouches and gear to be attached and removed without tools. In the Jeep world, it's become the standard for serious interior organization.</p>
<p>Bartact's <a href="https://bartact.com/collections/molle-accessories" rel="noopener">MOLLE accessories</a> are designed around the PALS webbing already built into their seat covers. If you're running Bartact seat backs with MOLLE panels, everything in their accessory line attaches to that webbing directly.</p>

<h2>The System</h2>
<p>MOLLE works because it's modular. You're not committing to a fixed organizer or a single layout. A pouch goes where you need it today and moves when your needs change. On a Wrangler or Gladiator, this matters — trail gear, first aid kits, recovery tools, hydration, and every-day carry items all compete for limited interior space. A MOLLE system on the seat backs opens up a storage surface that was previously just flat fabric.</p>
<p>The key is that the webbing has to be load-rated and properly spaced. Decorative webbing stitched on as an afterthought won't hold a loaded pouch under hard braking or over rough terrain. Bartact's MOLLE webbing is designed to PALS spec — 1-inch webbing on 1.5-inch centers, the same spacing that makes pouches from any manufacturer compatible.</p>

<h2>What Bartact Makes</h2>
<p>Beyond the seat back webbing built into their seat covers, Bartact makes standalone MOLLE accessories designed to work with the seat cover system and with each other. These include pouches sized for Wrangler and Gladiator applications, MOLLE panels that can be attached to additional surfaces, and hardware — buckles, clips, and connectors — for customizing the setup.</p>
<p>The <a href="https://bartact.com/collections/molle-accessories" rel="noopener">full MOLLE accessory lineup</a> is available on Bartact's site, with fitment notes for each product and the seat cover generations it's compatible with.</p>

<h2>Compatibility</h2>
<p>Because Bartact uses standard PALS spacing, their accessories are compatible with pouches and gear from other manufacturers that use the same system. This means you're not locked into a single brand's pouch lineup — any MOLLE-compatible pouch attaches to Bartact's webbing, and Bartact's MOLLE accessories attach to any PALS-spec webbing surface.</p>
<p>The practical implication: equip the seat backs with Bartact's seat covers and MOLLE webbing, then mix and match pouches from whatever sources meet your specific needs.</p>

<h2>Made in Temecula, CA</h2>
<p>Bartact's MOLLE accessories are manufactured in Temecula, California alongside the seat cover and grab handle lines. The quality control is consistent across the product family — same facility, same standards.</p>

<a class="bartact-link" href="https://bartact.com/collections/molle-accessories" rel="noopener"><span>Browse all Bartact MOLLE accessories →</span> Panels, pouches, buckles, and clips for Wrangler and Gladiator.</a>
</div>"""
)

# ── DOOR STORAGE BAGS ─────────────────────────────────────────────────────────
PAGES["door-storage-bags.html"] = page(
    "Wrangliator Door Storage Bags for Jeep Wrangler JL/JLU | Wrangliator",
    "Bartact Wrangliator door storage bags for Jeep Wrangler JL and JLU. Maximize door pocket utility. Made in Temecula, CA.",
    "door-storage-bags.html",
    """<div class="hero">
<h1>Door Storage Bags</h1>
<p>Wrangliator door bags for Jeep Wrangler JL/JLU. Made in Temecula, CA.</p>
</div>
<div class="container">
<p>The JL and JLU Wrangler's door pockets are usable but undersized for what most Wrangler owners actually carry. Bartact's Wrangliator door storage bags are designed to fit directly into the JL/JLU door pocket area, expanding the available storage without permanent modification to the door panel.</p>
<p>The bags are part of the Wrangliator product family — a name Bartact uses for JL/JLU-specific accessories that take advantage of the platform's updated interior architecture. For the full Wrangliator lineup, see <a href="https://bartact.com" rel="noopener">Bartact's product pages</a>.</p>

<h2>Why JL/JLU Door Pockets Are Underutilized</h2>
<p>The JL interior was a significant improvement over the JK in terms of layout and refinement, but the door pocket design leaves usable volume on the table. The pocket opening and shape don't lend themselves to the kind of gear Wrangler owners actually carry — water bottles, recovery tools, trail maps, or communications equipment tend to either not fit or rattle around.</p>
<p>Bartact's door bags solve this by filling the pocket space efficiently. The bags are shaped to the JL/JLU door pocket geometry, use the full available depth, and include organization features inside the bag itself — so you're not just filling the pocket, you're organizing it.</p>

<h2>JL and JLU Fitment</h2>
<p>The JLU (four-door) and JL (two-door) share the same front door pocket design, so the Wrangliator door bags fit both configurations in the front doors. Rear door fitment is JLU-specific since the two-door JL doesn't have rear doors. Check the product page for specific front versus rear fitment details.</p>

<h2>Removing the Doors</h2>
<p>Wrangler owners remove their doors. The Wrangliator door bags are designed with this reality in mind — the bags are easy to remove from the door pocket before the door comes off, and easy to reinstall when the doors go back on. They're not permanently attached to the door panel.</p>

<h2>Made in Temecula, CA</h2>
<p>Manufactured in-house at Bartact's Temecula, California facility alongside the rest of the Wrangler and Gladiator accessory lineup.</p>

<a class="bartact-link" href="https://bartact.com" rel="noopener"><span>Find Wrangliator door bags at Bartact →</span> JL and JLU fitment. Made in Temecula, CA.</a>
</div>"""
)

# ── FIRE EXTINGUISHER MOUNT ───────────────────────────────────────────────────
PAGES["fire-extinguisher-mount.html"] = page(
    "Roll Bar Fire Extinguisher Mount for Jeep Wrangler & Gladiator | Wrangliator",
    "Bartact roll bar fire extinguisher holders for Jeep Wrangler JK/JKU, JL/JLU, and Gladiator JT. Padded, secure, USA-made in Temecula, CA.",
    "fire-extinguisher-mount.html",
    """<div class="hero">
<h1>Roll Bar Fire Extinguisher Mount</h1>
<p>Padded roll bar holders for JKU/JK, JLU/JL, and Gladiator JT. Made in Temecula, CA.</p>
</div>
<div class="container">
<p>Mounting a fire extinguisher in a Wrangler or Gladiator is a safety decision many trail and overlanding Jeep owners make. The challenge is mounting it securely without it becoming a projectile in an accident or damaging the roll bar itself. Bartact's <a href="https://bartact.com/collections/roll-bar-fire-extinguisher-holder" rel="noopener">roll bar fire extinguisher holders</a> solve both problems.</p>

<h2>How It Works</h2>
<p>The holder wraps around the Wrangler or Gladiator roll bar using the same padded sleeve approach Bartact uses across the grab handle and roll bar accessory line. The interior of the sleeve is padded to protect the roll bar finish. The extinguisher is held by a heavy-duty retention strap that keeps it immobile over rough terrain — no rattling, no sliding, no contact between the extinguisher body and the roll bar metal.</p>
<p>Installation requires no drilling and no permanent modification. The sleeve mounts to the roll bar and locks with a closure system. It can be moved to different roll bar positions or removed entirely when not in use.</p>

<h2>Extinguisher Sizing</h2>
<p>The holder is designed for standard 1 lb and 2.5 lb fire extinguishers — the sizes most commonly used by off-road and overlanding Jeep owners. The 2.5 lb extinguisher is the more common choice for trail use, as it provides more suppression capacity than a 1 lb unit while still fitting the roll bar mounting format. Check the product page for the specific extinguisher diameter specifications the holder is designed for before purchasing a new extinguisher.</p>

<h2>Fitment</h2>
<p>Bartact's fire extinguisher holders fit the JKU and JK (2007–2018), JLU and JL (2018–present), and Gladiator JT (2020–present) roll bar diameters. The JKU and JLU are the more common configurations and are confirmed fitment — two-door JK and JL owners should verify roll bar diameter compatibility before ordering.</p>
<p>For the complete fire extinguisher holder lineup, see <a href="https://bartact.com/collections/roll-bar-fire-extinguisher-holder" rel="noopener">Bartact's roll bar fire extinguisher holder collection</a>.</p>

<h2>Trail Safety Context</h2>
<p>A fire extinguisher on the trail is a low-probability, high-consequence piece of safety equipment. Vehicle fires happen — from electrical shorts, fuel leaks after hard impacts, and brake or drivetrain failures under extreme use. Having an extinguisher accessible and secured in the cabin is the difference between a recoverable situation and a total loss. The roll bar mounting position keeps it within reach of both front seat occupants without taking up floor or console space.</p>

<h2>Made in Temecula, CA</h2>
<p>Manufactured in Temecula, California at Bartact's facility. Same quality standards as the rest of the roll bar accessory line.</p>

<a class="bartact-link" href="https://bartact.com/collections/roll-bar-fire-extinguisher-holder" rel="noopener"><span>Shop roll bar fire extinguisher holders →</span> JKU, JLU, JK, JL, Gladiator. Made in Temecula, CA.</a>
</div>"""
)

# ── SUN SHADES ────────────────────────────────────────────────────────────────
PAGES["sun-shades.html"] = page(
    "Tactical Sun Shades for Jeep Wrangler & Gladiator | Wrangliator",
    "Bartact tactical sun shades for Jeep Wrangler JK/JKU, JL/JLU, and Gladiator JT. Block heat and UV. Made in Temecula, CA.",
    "sun-shades.html",
    """<div class="hero">
<h1>Tactical Sun Shades</h1>
<p>JKU/JK, JLU/JL, and Gladiator JT. Blocks heat and UV. Made in Temecula, CA.</p>
</div>
<div class="container">
<p>A Wrangler or Gladiator with the top off or the doors removed in direct sun becomes a heat trap inside. The cabin absorbs solar radiation through the door openings and any remaining glass surfaces, and without a shade solution, interior temperatures climb fast — uncomfortable for passengers, damaging for electronics and gear left inside, and hard on the seat cover materials.</p>
<p>Bartact's tactical sun shades are designed for the Wrangler and Gladiator's specific door openings and dimensions. They're not a generic fold-out dashboard shade — they're built for the Jeep application.</p>

<h2>Fitment by Platform</h2>

<h3>JKU and JK Wrangler (2007–2018)</h3>
<p>The JK door opening dimensions are consistent across the production run. Bartact's sun shades for the JKU and JK fit the front door opening and, on the JKU, the rear door opening as well. The four-door JKU benefits more from rear sun shade coverage given the rear passenger exposure.</p>

<h3>JLU and JL Wrangler (2018–Present)</h3>
<p>The JL platform has larger door openings than the JK, particularly on the front doors, and Bartact's JL/JLU sun shades are patterned specifically for the JL door geometry. The JLU (four-door) has front and rear door shading options; the JL two-door applies to front doors only.</p>

<h3>Gladiator JT (2020–Present)</h3>
<p>The Gladiator shares its front door design with the JL, which means JL-spec front door sun shades apply to the JT as well. The Gladiator doesn't have rear passenger doors in the traditional Wrangler sense, so rear coverage is addressed differently.</p>

<h2>What Tactical Means Here</h2>
<p>Bartact's sun shades are built from the same materials and with the same attention to durability as the rest of their Wrangler accessory line. The shade material blocks UV and reduces heat transfer into the cabin. The attachment method is designed for a Wrangler owner who is taking doors on and off regularly — fast to install, fast to remove, no tools required.</p>
<p>The "tactical" label in the product family reflects the material and construction approach, not a marketing claim. These are working shades built for daily Wrangler use, not weekend-only accessories.</p>

<h2>Made in Temecula, CA</h2>
<p>Manufactured in Temecula, California alongside Bartact's full Wrangler and Gladiator lineup.</p>

<a class="bartact-link" href="https://bartact.com" rel="noopener"><span>Find Bartact sun shades →</span> JKU, JLU, JK, JL, Gladiator. Made in Temecula, CA.</a>
</div>"""
)

# ── SUSPENSION LIMIT STRAPS ───────────────────────────────────────────────────
PAGES["suspension-limit-straps.html"] = page(
    "Jeep Wrangler Suspension Limit Straps | Wrangliator",
    "Bartact suspension limit straps for Jeep Wrangler and Gladiator. Protect your suspension at full droop. Adjustable, heavy-duty, made in Temecula, CA.",
    "suspension-limit-straps.html",
    """<div class="hero">
<h1>Suspension Limit Straps</h1>
<p>Protect your suspension at full droop. Wrangler and Gladiator. Made in Temecula, CA.</p>
</div>
<div class="container">
<p>Suspension limit straps are a straightforward piece of off-road safety equipment: they prevent the suspension from overextending at full droop, protecting your CV axles, brake lines, and steering components from the damage that comes with unchecked suspension travel.</p>
<p>On a lifted Wrangler or Gladiator with long-travel suspension, full droop without limits puts significant stress on every flexible component in the front and rear axle area. A blown CV axle mid-trail is a much worse outcome than adding limit straps before the trip. Bartact's <a href="https://bartact.com/collections/jeep-wrangler-suspension-limit-straps" rel="noopener">Jeep Wrangler suspension limit straps</a> are designed for this application.</p>

<h2>What They Do</h2>
<p>The strap connects between the frame and the axle housing. When the suspension reaches full droop, the strap goes taut and stops the travel at that point. The key variable is strap length — too short and you're limiting travel unnecessarily; too long and you're not providing meaningful protection before your vulnerable components reach their limits.</p>
<p>Bartact's limit straps are adjustable, which allows you to dial in the correct droop limit for your specific lift height and suspension setup rather than being locked into a fixed length.</p>

<h2>Wrangler and Gladiator Fitment</h2>
<p>Limit strap fitment depends on lift height and axle configuration more than specific Wrangler generation. Bartact's straps are designed for the Wrangler and Gladiator platform axle mounting points. The product page at <a href="https://bartact.com/collections/jeep-wrangler-suspension-limit-straps" rel="noopener">Bartact's limit strap collection</a> includes fitment guidance and sizing recommendations based on lift height.</p>

<h2>Construction</h2>
<p>Heavy-duty webbing, reinforced end loops, and adjustable length. The construction priorities are the same as the rest of the Bartact accessory line — durability under load and resistance to the elements that a Wrangler suspension sees on the trail: mud, water, UV, and repeated high-load cycling as the suspension works through terrain.</p>

<h2>Made in Temecula, CA</h2>
<p>Manufactured in Temecula, California. Same facility, same standards as the rest of the Bartact Wrangler and Gladiator lineup.</p>

<a class="bartact-link" href="https://bartact.com/collections/jeep-wrangler-suspension-limit-straps" rel="noopener"><span>Shop Bartact suspension limit straps →</span> Adjustable, heavy-duty, made in Temecula, CA.</a>
</div>"""
)

# ── CONSOLE ORGANIZERS ────────────────────────────────────────────────────────
PAGES["console-organizers.html"] = page(
    "Console Organizers & Storage Bags for Jeep Wrangler & Gladiator | Wrangliator",
    "Bartact console organizers and storage bags for Jeep Wrangler and Gladiator. Maximize interior storage. Made in Temecula, CA.",
    "console-organizers.html",
    """<div class="hero">
<h1>Console Organizers & Storage Bags</h1>
<p>Maximize interior storage for Wrangler and Gladiator. Made in Temecula, CA.</p>
</div>
<div class="container">
<p>The Wrangler interior has always traded passenger comfort for capability, and storage organization is a perennial challenge. The console area in the JK and JL platforms has improved with each generation, but the stock layout still leaves useful space underutilized — particularly once you start carrying the kind of gear that trail driving and overlanding require.</p>
<p>Bartact makes console organizers and interior storage solutions specifically for the Wrangler and Gladiator platforms. Like the rest of the product line, these are purpose-built for the Jeep application — not universal accessories that are adapted to fit.</p>

<h2>The Organization Problem</h2>
<p>On the trail, loose gear in a Wrangler cabin is a real issue. Hard braking on a descent, a sudden articulation event, or a recovery situation that puts the Jeep at a steep angle — everything that isn't secured becomes a problem. Organized storage keeps gear where it belongs and accessible when you need it quickly.</p>
<p>The Bartact storage bag and organizer lineup addresses both the center console area and other interior storage zones in the Wrangler and Gladiator. Products are sized and shaped for the specific interior geometry of each platform generation.</p>

<h2>Integrating with the MOLLE System</h2>
<p>Many of Bartact's storage and organizer solutions are designed to work with the MOLLE system built into their seat covers. Pouches and bags that attach to the seat back MOLLE webbing are covered in the <a href="/molle-accessories.html">MOLLE accessories guide</a>. Console-area solutions are standalone, working with the console architecture of the specific Wrangler or Gladiator generation.</p>

<h2>Gladiator Considerations</h2>
<p>The Gladiator JT shares much of its interior architecture with the JL Wrangler, which means JL-spec console solutions often apply to the JT as well. However, the Gladiator's truck bed configuration changes some of the storage priorities — what you carry in the cab versus the bed shifts the calculus on interior organization compared to a Wrangler.</p>

<h2>Made in Temecula, CA</h2>
<p>All storage and organizer products are manufactured at Bartact's Temecula, California facility. For the full lineup of console and interior storage solutions, see <a href="https://bartact.com" rel="noopener">Bartact's product collection</a>.</p>

<a class="bartact-link" href="https://bartact.com" rel="noopener"><span>Find Bartact console and storage products →</span> Wrangler and Gladiator specific. Made in Temecula, CA.</a>
</div>"""
)

# ── 550 PARACORD ──────────────────────────────────────────────────────────────
PAGES["550-paracord.html"] = page(
    "USA-Sourced 550 Paracord — The Material Behind Bartact Grab Handles | Wrangliator",
    "Bartact uses USA-sourced 550 paracord in their Jeep grab handles. Learn what 550 paracord is, why it matters, and where to get it from Bartact.",
    "550-paracord.html",
    """<div class="hero">
<h1>550 Paracord</h1>
<p>USA-sourced. The material behind Bartact's grab handles. What it is and why it matters.</p>
</div>
<div class="container">
<p>Bartact sources 550 paracord in the USA for use in their <a href="/paracord-grab-handles.html">paracord grab handles</a>. If you want the paracord itself — either for Jeep use or for other applications — Bartact makes it available directly through their site.</p>

<h2>What 550 Paracord Is</h2>
<p>550 paracord is a type of nylon kernmantle rope — a braided outer sheath (the mantle) surrounding a core of inner strands (the kern). "550" refers to the minimum breaking strength: 550 pounds. The standard construction includes seven inner strands, each of which is itself a braided structure. The inner strands can be removed from the outer sheath for use independently in situations where thinner cordage is needed.</p>
<p>The material is UV-resistant, mold-resistant, and maintains its strength and flexibility across temperature extremes. It stretches slightly under load before returning to its original length, which gives it some shock-absorption capacity that stiffer materials don't have.</p>

<h2>Type III Military Spec</h2>
<p>The paracord Bartact uses meets Type III military specification — the standard that defines the 550 lb minimum breaking strength, the seven inner strand requirement, and the allowable elongation characteristics. Not all paracord sold as "550" meets this specification — the designation has been applied loosely in the consumer market. USA-sourced paracord from domestic manufacturers is more reliably consistent with the Type III spec than imported alternatives.</p>

<h2>Why It Works for Grab Handles</h2>
<p>For a grab handle application, the relevant properties are breaking strength, UV resistance, and durability across temperature cycles. A Wrangler roll bar in direct sun gets hot — materials that soften or degrade under sustained UV exposure and heat are a problem. Paracord handles this well: the nylon construction is UV-stable, and the round cross-section that looks purely decorative is actually ergonomically comfortable as a grip surface.</p>
<p>The weight is also right for the application. Paracord grips don't add meaningful weight to the vehicle, and the braided construction gives them a natural texture that improves grip without requiring a rubberized coating that might crack or peel over time.</p>

<h2>Available from Bartact</h2>
<p>Bartact makes their USA-sourced 550 paracord available for purchase directly — either because you want to use it for projects beyond the Jeep, or because you want to replace grab handle material on existing handles. See the <a href="https://bartact.com/collections/paracord-grab-handles" rel="noopener">paracord section on Bartact's site</a> for availability and color options.</p>

<h2>Made and Sourced in the USA</h2>
<p>The paracord Bartact uses is USA-sourced. This is consistent with the broader manufacturing philosophy at Bartact — the finished accessories are made in Temecula, California, and the materials they're made from are sourced domestically where possible.</p>

<a class="bartact-link" href="https://bartact.com/collections/paracord-grab-handles" rel="noopener"><span>Shop 550 paracord at Bartact →</span> USA-sourced. Available in multiple colors.</a>
</div>"""
)

# ── WRITE FILES ────────────────────────────────────────────────────────────────
for filename, html in PAGES.items():
    filepath = os.path.join(SITE_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(html)
    words = len(html.split())
    print(f"✅ {filename}: ~{words} words")

# robots.txt
with open(os.path.join(SITE_DIR, 'robots.txt'), 'w') as f:
    f.write("User-agent: *\nAllow: /\nSitemap: https://wrangliator.com/sitemap.xml\n")

# sitemap.xml
slugs = [("", "1.0"), ("jeep-wrangler-seat-covers.html","0.9"), 
         ("paracord-grab-handles.html","0.9"), ("molle-accessories.html","0.8"),
         ("door-storage-bags.html","0.8"), ("fire-extinguisher-mount.html","0.8"),
         ("sun-shades.html","0.8"), ("suspension-limit-straps.html","0.8"),
         ("console-organizers.html","0.8"), ("550-paracord.html","0.7")]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for slug, priority in slugs:
    url = f"https://wrangliator.com/{slug}"
    sitemap += f"<url><loc>{url}</loc><priority>{priority}</priority></url>\n"
sitemap += "</urlset>"
with open(os.path.join(SITE_DIR, 'sitemap.xml'), 'w') as f:
    f.write(sitemap)

print("\n✅ All files written")
print(f"Total pages: {len(PAGES)}")
