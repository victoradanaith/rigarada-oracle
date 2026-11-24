import sys
out = []
def cat(name, lines):
    out.append('# ' + name)
    for l in lines.strip().split('\n'):
        l = l.strip()
        if not l: continue
        th, en, kw = l.split('|')
        out.append(f'{th}|{en}|{kw}||')

cat('มือหนึ่งหรือมือสอง', """
ควรซื้อรถมือหนึ่ง|Buy a new car|มือหนึ่ง,ควรซื้อ
ควรซื้อรถมือสอง|Buy a used car|มือสอง,ควรซื้อ
มือหนึ่งคุ้มกว่า|A new car is better value|มือหนึ่ง,คุ้มค่า
มือสองคุ้มกว่า|A used car is better value|มือสอง,คุ้มค่า
รถมือสองสภาพดีรออยู่|A good used car is waiting|มือสอง,โอกาสดี
รถมือสองมีประวัติซ่อมหนัก|The used car has a heavy repair history|มือสอง,ระวัง
รถมือสองเคยจมน้ำ|The used car was once flooded|มือสอง,ระวัง
รถมือสองเคยชนหนัก|The used car was in a bad crash|มือสอง,ระวัง
รถมือสองเจ้าของเดียว|One-owner used car|มือสอง,ดี
รถมือสองเปลี่ยนมือหลายครั้ง|The used car has had many owners|มือสอง,ระวัง
รถมือสองไมล์น้อย|Low-mileage used car|มือสอง,ดี
รถมือสองไมล์ถูกกรอ|The odometer was wound back|มือสอง,ระวัง
รถมือสองราคาดีกว่าตลาด|Used car priced below market|มือสอง,คุ้มค่า
รถมือสองราคาถูกผิดปกติ|Suspiciously cheap used car|มือสอง,ระวัง
รถป้ายแดงได้เปรียบ|A brand-new car has the edge|มือหนึ่ง,ดี
รถมือหนึ่งราคาตกเร็ว|A new car loses value fast|มือหนึ่ง,ข้อเสีย
รถมือหนึ่งได้ของแถมเยอะ|Lots of extras with a new car|มือหนึ่ง,โปรโมชัน
รถมือหนึ่งรอคิวนาน|Long wait for the new car|มือหนึ่ง,รอ
รถมือหนึ่งมีประกันจากศูนย์|New car comes with dealer warranty|มือหนึ่ง,ประกัน
รถมือสองยังเหลือประกันศูนย์|Used car still under warranty|มือสอง,ประกัน
รถมือสองจากคนรู้จัก|Used car from someone you know|มือสอง,คนรู้จัก
รถมือสองจากเต็นท์|Used car from a dealer lot|มือสอง,เต็นท์
รถมือสองประมูล|Auction car|มือสอง,ประมูล
รถมือสองนำเข้า|Imported used car|มือสอง,นำเข้า
รถป้ายแดงตัวโชว์|Showroom demo car|มือหนึ่ง,ราคาพิเศษ
รถค้างสต็อกปีเก่า|Last year's unsold stock|มือหนึ่ง,ราคาพิเศษ
รถรุ่นใหม่เพิ่งเปิดตัว|Model just launched|มือหนึ่ง,รุ่นใหม่
รถรุ่นเก่าใกล้เปลี่ยนโฉม|Old model about to be replaced|มือหนึ่ง,รอ
ซื้อรถต่อจากญาติ|Take over a relative's car|มือสอง,ครอบครัว
เช่าขับก่อนตัดสินใจ|Rent one before you decide|ลองก่อน,ควรรอ
""")

types = [('รถเก๋ง','a sedan'),('รถกระบะ','a pickup'),('รถ SUV','an SUV'),('รถตู้','a van'),
         ('รถไฟฟ้า','an electric car'),('รถไฮบริด','a hybrid'),('รถอีโคคาร์','an eco car'),
         ('รถสปอร์ต','a sports car'),('รถหรู','a luxury car'),('รถ 7 ที่นั่ง','a seven-seater'),
         ('รถญี่ปุ่น','a Japanese car'),('รถยุโรป','a European car'),('รถจีน','a Chinese car')]
vs = [('ซื้อ{t}ได้','Go ahead and buy {e}','ควรซื้อ'),('ยังไม่ควรซื้อ{t}','Not yet for {e}','ยังไม่ควร'),
      ('{t}เหมาะกับคุณ','{E} suits you','เหมาะ'),('{t}ไม่เหมาะกับคุณ','{E} does not suit you','ไม่เหมาะ'),
      ('{t}คุ้มค่า','{E} is good value','คุ้มค่า')]
out.append('# ประเภทรถ')
for t, e in types:
    E = e[0].upper() + e[1:]
    for th, en, k in vs:
        out.append(f"{th.format(t=t)}|{en.format(e=e, E=E)}|{k},{t}||")

cat('จังหวะเวลา ควรซื้อ ควรรอ', """
ซื้อได้เลยตอนนี้|Buy now|ควรซื้อ,จังหวะ
ควรรอก่อน|Wait for now|ควรรอ,จังหวะ
ไม่ควรรอ|Don't wait|ไม่ควรรอ,จังหวะ
รองานมอเตอร์โชว์|Wait for the motor show|ควรรอ,โปรโมชัน
รอโปรปลายปี|Wait for year-end deals|ควรรอ,โปรโมชัน
ซื้อช่วงต้นปีดี|Early in the year is good|จังหวะ,ต้นปี
ซื้อช่วงกลางปีดี|Mid-year is good|จังหวะ,กลางปี
ซื้อช่วงปลายปีดี|Late in the year is good|จังหวะ,ปลายปี
รอรุ่นใหม่ออกก่อน|Wait for the new model|ควรรอ,รุ่นใหม่
ซื้อก่อนราคาขึ้น|Buy before the price goes up|ไม่ควรรอ,ราคา
รอราคาลง|Wait for the price to drop|ควรรอ,ราคา
รอให้เงินเก็บพอก่อน|Save enough first|ควรรอ,การเงิน
รองานมั่นคงก่อน|Wait until your job is steady|ควรรอ,งาน
รอย้ายบ้านเสร็จก่อน|Wait until the move is done|ควรรอ,บ้าน
ซื้อก่อนลูกเข้าโรงเรียน|Buy before the kids start school|จังหวะ,ครอบครัว
ซื้อก่อนแต่งงาน|Buy before the wedding|จังหวะ,ความรัก
รอหลังแต่งงาน|Wait until after the wedding|ควรรอ,ความรัก
จังหวะกำลังดี|The timing is right|จังหวะ,ดี
พลาดจังหวะไปแล้ว|You missed the moment|จังหวะ,พลาด
อีกไม่นานได้รถ|A car is coming soon|เร็วๆ นี้,ได้รถ
ภายใน 3 เดือนได้รถ|A car within 3 months|ระยะเวลา,ได้รถ
ภายใน 1 ปีได้รถ|A car within a year|ระยะเวลา,ได้รถ
รถคันเดิมยังใช้ได้อีกนาน|Your car has years left|ควรรอ,รถเดิม
ถึงเวลาเปลี่ยนรถ|Time for a new car|ควรซื้อ,เปลี่ยนรถ
รอนโยบายรถไฟฟ้าชัดก่อน|Wait for clear EV policy|ควรรอ,รถไฟฟ้า
อย่าตัดสินใจตอนอารมณ์ร้อน|Don't decide in the heat of the moment|ควรรอ,สติ
ตัดสินใจเร็วได้ของดี|A quick decision lands a good one|ไม่ควรรอ,โอกาส
รอคนในบ้านเห็นด้วยก่อน|Wait until the family agrees|ควรรอ,ครอบครัว
ไปดูรถหลายที่ก่อน|Look at several places first|ควรรอ,เปรียบเทียบ
คันที่ใช่ยังไม่มา|The right car hasn't come yet|ควรรอ,รถที่ใช่
คันที่ใช่อยู่ตรงหน้า|The right car is right here|ควรซื้อ,รถที่ใช่
จองไว้ก่อนได้|You can book it now|ควรซื้อ,จอง
ยกเลิกการจองดีกว่า|Better to cancel the booking|ยกเลิก,ระวัง
รอให้ปีชงผ่านไปก่อน|Wait until your clash year passes|ควรรอ,ความเชื่อ
รอวันฤกษ์ดีค่อยรับรถ|Take delivery on an auspicious day|ควรรอ,ความเชื่อ
""")

cat('การเงิน ซื้อสด ผ่อน ดาวน์', """
ควรซื้อสด|Pay cash|ซื้อสด,การเงิน
ควรผ่อน|Pay in instalments|ผ่อน,การเงิน
ซื้อสดได้ส่วนลด|Cash gets a discount|ซื้อสด,ส่วนลด
ผ่อนแล้วสบายกว่า|Instalments are easier on you|ผ่อน,ดี
ผ่อนไหว|You can afford the payments|ผ่อน,ไหว
ผ่อนไม่ไหว|You can't afford the payments|ผ่อน,ไม่ไหว
ดาวน์ไหว|You can manage the down payment|ดาวน์,ไหว
ดาวน์ไม่ไหว|The down payment is too much|ดาวน์,ไม่ไหว
ดาวน์เยอะผ่อนน้อย|Big deposit, small payments|ดาวน์,ผ่อน
ดาวน์น้อยผ่อนนาน|Small deposit, long loan|ดาวน์,ผ่อน
ไฟแนนซ์อนุมัติ|The car loan is approved|ไฟแนนซ์,ผ่าน
ไฟแนนซ์ไม่อนุมัติ|The car loan is turned down|ไฟแนนซ์,ไม่ผ่าน
ได้ดอกเบี้ยต่ำ|You get a low rate|ดอกเบี้ย,ดี
ดอกเบี้ยแพงเกินไป|The rate is too high|ดอกเบี้ย,ระวัง
ผ่อนศูนย์เปอร์เซ็นต์|Zero-interest deal|ดอกเบี้ย,โปรโมชัน
ผ่อนสั้นดีกว่า|A shorter loan is better|ผ่อน,ระยะเวลา
ผ่อนยาวสบายกระเป๋า|A longer loan is easier|ผ่อน,ระยะเวลา
ปิดไฟแนนซ์ก่อนกำหนดได้|You can pay off early|ไฟแนนซ์,ปิดยอด
ต้องมีคนค้ำประกัน|You need a guarantor|ไฟแนนซ์,คนค้ำ
อย่าค้ำประกันรถให้ใคร|Don't guarantee anyone's car loan|คนค้ำ,ระวัง
ใช้เงินเก็บซื้อ|Buy with savings|ซื้อสด,เงินเก็บ
อย่าใช้เงินฉุกเฉินซื้อรถ|Don't use your emergency fund|เงินเก็บ,ระวัง
มีผู้ใหญ่ช่วยออกเงิน|An elder helps pay|การเงิน,ผู้ใหญ่
ได้เงินก้อนมาซื้อรถ|A lump sum comes for the car|การเงิน,โชคลาภ
งบเกินที่ตั้งไว้|Over budget|งบ,ระวัง
อยู่ในงบพอดี|Right on budget|งบ,ดี
ลดสเปกแล้วคุ้มกว่า|A lower trim is better value|งบ,คุ้มค่า
เพิ่มงบอีกนิดได้คันที่ดีกว่า|A bit more buys a better car|งบ,คุ้มค่า
ค่าผ่อนกินเงินเดือนเกินไป|Payments eat too much of your pay|ผ่อน,ระวัง
ต่อรองราคาได้|You can bargain|ต่อรอง,ส่วนลด
ต่อรองไม่ได้|No room to bargain|ต่อรอง,ราคา
ได้ของแถมคุ้ม|Worthwhile extras|โปรโมชัน,คุ้มค่า
ของแถมไม่คุ้ม|The extras aren't worth it|โปรโมชัน,ไม่คุ้ม
รีไฟแนนซ์ช่วยได้|Refinancing helps|ไฟแนนซ์,รีไฟแนนซ์
ระวังค่าธรรมเนียมแฝง|Watch for hidden fees|ค่าธรรมเนียม,ระวัง
ลีสซิ่งดีกว่าซื้อ|Leasing beats buying|ลีสซิ่ง,ทางเลือก
ซื้อดีกว่าลีสซิ่ง|Buying beats leasing|ลีสซิ่ง,ทางเลือก
เช่ารถรายเดือนคุ้มกว่า|Monthly rental is better value|เช่า,ทางเลือก
ยังไม่ต้องมีรถก็ได้|You don't need a car yet|ทางเลือก,ควรรอ
ใช้รถร่วมกับคนในบ้าน|Share a car with family|ทางเลือก,ครอบครัว
""")

cat('สภาพรถดีหรือไม่ดี', """
รถคันนี้ดี|This car is good|รถดี,ตัดสินใจ
รถคันนี้ไม่ดี|This car is not good|รถไม่ดี,ตัดสินใจ
เครื่องยนต์แข็งแรง|Strong engine|รถดี,เครื่องยนต์
เครื่องยนต์มีปัญหา|Engine trouble|รถไม่ดี,เครื่องยนต์
เกียร์นุ่ม|Smooth gearbox|รถดี,เกียร์
เกียร์กระตุก|Jerky gearbox|รถไม่ดี,เกียร์
ช่วงล่างแน่น|Solid suspension|รถดี,ช่วงล่าง
ช่วงล่างหลวม|Loose suspension|รถไม่ดี,ช่วงล่าง
เบรกดี|Good brakes|รถดี,เบรก
เบรกต้องซ่อม|Brakes need work|รถไม่ดี,เบรก
แอร์เย็นฉ่ำ|Ice-cold air-con|รถดี,แอร์
แอร์ไม่เย็น|Air-con doesn't cool|รถไม่ดี,แอร์
ระบบไฟฟ้าปกติ|Electrics are fine|รถดี,ระบบไฟ
ระบบไฟฟ้ารวน|Electrical faults|รถไม่ดี,ระบบไฟ
แบตเตอรี่รถไฟฟ้ายังดี|EV battery still healthy|รถดี,แบตเตอรี่
แบตเตอรี่รถไฟฟ้าเสื่อม|EV battery worn|รถไม่ดี,แบตเตอรี่
ตัวถังเดิมไม่เคยทำสี|Original paint, never resprayed|รถดี,ตัวถัง
ตัวถังมีสนิม|Rust on the body|รถไม่ดี,ตัวถัง
ห้องโดยสารสะอาด|Clean cabin|รถดี,ภายใน
ห้องโดยสารมีกลิ่นอับ|Musty cabin|รถไม่ดี,ภายใน
ยางยังใหม่|Tyres still new|รถดี,ยาง
ยางต้องเปลี่ยน|Tyres need replacing|รถไม่ดี,ยาง
ประหยัดน้ำมัน|Easy on fuel|รถดี,ประหยัด
กินน้ำมัน|Thirsty|รถไม่ดี,สิ้นเปลือง
ขับนิ่ม|Comfortable ride|รถดี,การขับขี่
ขับแข็งกระด้าง|Harsh ride|รถไม่ดี,การขับขี่
เสียงเงียบ|Quiet|รถดี,เสียง
มีเสียงแปลก|Strange noises|รถไม่ดี,เสียง
อะไหล่หาง่าย|Parts are easy to find|รถดี,อะไหล่
อะไหล่หายาก|Parts are hard to find|รถไม่ดี,อะไหล่
ศูนย์บริการใกล้บ้าน|Service centre near home|รถดี,ศูนย์บริการ
ศูนย์บริการไกล|Service centre is far away|รถไม่ดี,ศูนย์บริการ
ระบบความปลอดภัยครบ|Full safety kit|รถดี,ความปลอดภัย
ระบบความปลอดภัยน้อย|Few safety features|รถไม่ดี,ความปลอดภัย
ราคาขายต่อดี|Holds its resale value|รถดี,ขายต่อ
ราคาขายต่อตก|Poor resale value|รถไม่ดี,ขายต่อ
รุ่นนี้ทนทาน|This model is durable|รถดี,ทนทาน
รุ่นนี้มีปัญหาจุกจิก|This model has niggles|รถไม่ดี,จุกจิก
ห้องโดยสารกว้าง|Roomy cabin|รถดี,พื้นที่
ห้องโดยสารคับแคบ|Cramped cabin|รถไม่ดี,พื้นที่
ขับง่ายจอดง่าย|Easy to drive and park|รถดี,ขับง่าย
คันใหญ่เกินไปสำหรับคุณ|Too big for you|รถไม่ดี,ขนาด
ผ่านการตรวจสภาพ|Passes inspection|รถดี,ตรวจสภาพ
ควรให้ช่างตรวจก่อน|Have a mechanic check it first|ตรวจสภาพ,ระวัง
ลองขับแล้วใช่|The test drive feels right|ทดลองขับ,ดี
""")

cat('ผู้ขาย เต็นท์ และเอกสาร', """
เซลส์จริงใจ|An honest salesperson|ผู้ขาย,ดี
เซลส์พูดเกินจริง|The salesperson oversells|ผู้ขาย,ระวัง
เต็นท์น่าเชื่อถือ|A trustworthy lot|เต็นท์,ดี
เต็นท์ไม่น่าไว้ใจ|An untrustworthy lot|เต็นท์,ระวัง
โชว์รูมให้ดีลดี|The showroom gives a good deal|โชว์รูม,ส่วนลด
ไปอีกโชว์รูมได้ราคาดีกว่า|Another showroom is cheaper|โชว์รูม,เปรียบเทียบ
ซื้อจากเจ้าของโดยตรงดี|Buy straight from the owner|ผู้ขาย,มือสอง
ผู้ขายรีบขายผิดสังเกต|The seller is oddly in a hurry|ผู้ขาย,ระวัง
เล่มทะเบียนครบถ้วน|Registration book in order|เอกสาร,ดี
เล่มทะเบียนมีปัญหา|Problem with the registration book|เอกสาร,ระวัง
รถติดไฟแนนซ์เดิม|Car still has a loan on it|เอกสาร,ระวัง
ตรวจเลขตัวถังให้ตรง|Check the chassis number matches|เอกสาร,ตรวจสอบ
ภาษีรถยังไม่ขาด|Road tax is up to date|เอกสาร,ดี
ภาษีรถค้างจ่าย|Road tax is overdue|เอกสาร,ระวัง
โอนรถเรียบร้อย|Transfer goes smoothly|โอน,ดี
โอนรถล่าช้า|Transfer is delayed|โอน,ล่าช้า
อ่านสัญญาให้ละเอียด|Read the contract carefully|สัญญา,ระวัง
สัญญาเป็นธรรม|A fair contract|สัญญา,ดี
ระวังรถโจรกรรม|Watch out for stolen cars|ผิดกฎหมาย,ระวัง
ระวังรถสวมทะเบียน|Watch out for cloned plates|ผิดกฎหมาย,ระวัง
ระวังโอนเงินมัดจำออนไลน์|Careful with online deposits|มิจฉาชีพ,ระวัง
ได้รถตรงตามสเปก|The car matches the spec|รับรถ,ดี
รับรถแล้วไม่ตรงปก|The car isn't as described|รับรถ,ระวัง
ตรวจรถก่อนเซ็นรับ|Inspect before you sign|รับรถ,ตรวจสอบ
ได้รับรถตรงเวลา|Delivered on time|รับรถ,ตรงเวลา
รับรถล่าช้า|Late delivery|รับรถ,ล่าช้า
มีคนรู้จักช่วยดูรถ|Someone you know helps you look|คนช่วย,ดี
คนแนะนำได้ค่าคอมแอบแฝง|The person recommending gets a cut|คนกลาง,ระวัง
ประกันชั้นหนึ่งแถมฟรี|Free first-class insurance|ประกัน,โปรโมชัน
รับประกันหลังการขายดี|Good after-sales warranty|ประกัน,ดี
""")

cat('สีรถ', """
รถสีขาว|White car|สีรถ,ขาว
รถสีดำ|Black car|สีรถ,ดำ
รถสีเทา|Grey car|สีรถ,เทา
รถสีบรอนซ์เงิน|Silver car|สีรถ,เงิน
รถสีแดง|Red car|สีรถ,แดง
รถสีน้ำเงิน|Dark blue car|สีรถ,น้ำเงิน
รถสีฟ้า|Light blue car|สีรถ,ฟ้า
รถสีเขียว|Green car|สีรถ,เขียว
รถสีเหลือง|Yellow car|สีรถ,เหลือง
รถสีส้ม|Orange car|สีรถ,ส้ม
รถสีชมพู|Pink car|สีรถ,ชมพู
รถสีม่วง|Purple car|สีรถ,ม่วง
รถสีน้ำตาล|Brown car|สีรถ,น้ำตาล
รถสีทอง|Gold car|สีรถ,ทอง
รถสีครีม|Cream car|สีรถ,ครีม
สีรถเป็นมงคลกับคุณ|The colour is lucky for you|สีรถ,มงคล
สีรถไม่ถูกโฉลกกับคุณ|The colour isn't lucky for you|สีรถ,ไม่ถูกโฉลก
สีนี้ขายต่อได้ราคา|This colour resells well|สีรถ,ขายต่อ
สีนี้ขายต่อยาก|This colour is hard to resell|สีรถ,ขายต่อ
สีนี้ดูแลง่าย|This colour is easy to keep clean|สีรถ,ดูแล
สีนี้เห็นรอยง่าย|This colour shows every mark|สีรถ,ดูแล
สีอ่อนไม่ร้อน|A light colour stays cool|สีรถ,ร้อน
สีเข้มเก็บความร้อน|A dark colour gets hot|สีรถ,ร้อน
สีสดเห็นชัดปลอดภัย|A bright colour is easier to see|สีรถ,ความปลอดภัย
สีที่ใจชอบที่สุดคือสีที่ใช่|The colour you love most is the one|สีรถ,ใจ
สีที่คนในบ้านชอบ|The colour your family likes|สีรถ,ครอบครัว
ติดฟิล์มสีมงคล|Lucky-coloured window tint|สีรถ,ความเชื่อ
""")

# taksa colours by birth day
RING = ['อาทิตย์','จันทร์','อังคาร','พุธ','เสาร์','พฤหัสบดี','ราหู','ศุกร์']
PCOL = {'อาทิตย์':('แดง','red'),'จันทร์':('เหลืองครีม','yellow or cream'),'อังคาร':('ชมพู','pink'),
        'พุธ':('เขียว','green'),'พฤหัสบดี':('ส้ม','orange'),'ศุกร์':('ฟ้า','light blue'),
        'เสาร์':('ม่วง','purple'),'ราหู':('เทาดำ','grey or black')}
DAYS = [('อาทิตย์','อาทิตย์','Sunday'),('จันทร์','จันทร์','Monday'),('อังคาร','อังคาร','Tuesday'),
        ('พุธกลางวัน','พุธ','Wednesday daytime'),('พุธกลางคืน','ราหู','Wednesday night'),
        ('พฤหัสบดี','พฤหัสบดี','Thursday'),('ศุกร์','ศุกร์','Friday'),('เสาร์','เสาร์','Saturday')]
ROLES = [('บริวาร',0,'helpers'),('เดช',2,'power'),('ศรี',3,'fortune'),('มนตรี',6,'support'),('กาลกิณี',7,'bad luck')]
out.append('# สีถูกโฉลกตามวันเกิด')
for dname, planet, en in DAYS:
    i = RING.index(planet)
    for role, off, ren in ROLES:
        p = RING[(i + off) % 8]
        c, ce = PCOL[p]
        if role == 'กาลกิณี':
            out.append(f'คนเกิดวัน{dname}เลี่ยงรถสี{c}|{en}-born: avoid a {ce} car ({ren})|สีถูกโฉลก,{role}||')
        else:
            out.append(f'คนเกิดวัน{dname}รถสี{c}เสริม{role}|{en}-born: a {ce} car brings {ren}|สีถูกโฉลก,{role}||')

cat('สีตามธาตุจีน', """
ธาตุไม้เสริมด้วยรถสีเขียว|Wood element: a green car helps|ธาตุ,ไม้
ธาตุไม้เสริมด้วยรถสีดำหรือน้ำเงิน|Wood element: black or blue helps|ธาตุ,ไม้
ธาตุไม้เลี่ยงรถสีขาวหรือเงิน|Wood element: avoid white or silver|ธาตุ,ไม้
ธาตุไฟเสริมด้วยรถสีแดง|Fire element: a red car helps|ธาตุ,ไฟ
ธาตุไฟเสริมด้วยรถสีเขียว|Fire element: green helps|ธาตุ,ไฟ
ธาตุไฟเลี่ยงรถสีดำหรือน้ำเงิน|Fire element: avoid black or blue|ธาตุ,ไฟ
ธาตุดินเสริมด้วยรถสีเหลืองหรือน้ำตาล|Earth element: yellow or brown helps|ธาตุ,ดิน
ธาตุดินเสริมด้วยรถสีแดง|Earth element: red helps|ธาตุ,ดิน
ธาตุดินเลี่ยงรถสีเขียว|Earth element: avoid green|ธาตุ,ดิน
ธาตุทองเสริมด้วยรถสีขาวหรือเงิน|Metal element: white or silver helps|ธาตุ,ทอง
ธาตุทองเสริมด้วยรถสีเหลืองหรือน้ำตาล|Metal element: yellow or brown helps|ธาตุ,ทอง
ธาตุทองเลี่ยงรถสีแดง|Metal element: avoid red|ธาตุ,ทอง
ธาตุน้ำเสริมด้วยรถสีดำหรือน้ำเงิน|Water element: black or blue helps|ธาตุ,น้ำ
ธาตุน้ำเสริมด้วยรถสีขาวหรือเงิน|Water element: white or silver helps|ธาตุ,น้ำ
ธาตุน้ำเลี่ยงรถสีเหลืองหรือน้ำตาล|Water element: avoid yellow or brown|ธาตุ,น้ำ
ปีนักษัตรถูกกับรถคันนี้|Your zodiac year suits this car|นักษัตร,ถูกโฉลก
ปีนักษัตรชงกับวันรับรถ|Delivery day clashes with your sign|นักษัตร,ปีชง
""")

cat('ทะเบียนและเลขมงคล', """
ได้ทะเบียนเลขสวย|You get a nice plate number|ทะเบียน,เลขมงคล
ประมูลทะเบียนได้|You win the plate auction|ทะเบียน,ประมูล
ทะเบียนผลรวมดี|The plate digits add up well|ทะเบียน,ผลรวม
ทะเบียนผลรวมไม่ดี|The plate digits add up badly|ทะเบียน,ผลรวม
ทะเบียนมีเลขเก้า|A plate with nine|ทะเบียน,เลข 9
ทะเบียนมีเลขแปด|A plate with eight|ทะเบียน,เลข 8
ทะเบียนมีเลขหก|A plate with six|ทะเบียน,เลข 6
ทะเบียนเลขเบิ้ล|A plate with repeated digits|ทะเบียน,เลขเบิ้ล
ทะเบียนเลขเรียง|A plate with a sequence|ทะเบียน,เลขเรียง
ทะเบียนตรงวันเกิด|Plate matches your birthday|ทะเบียน,วันเกิด
หมวดอักษรทะเบียนดี|Lucky plate letters|ทะเบียน,อักษร
หมวดอักษรทะเบียนเป็นกาลกิณี|Plate letters are your bad-luck letters|ทะเบียน,กาลกิณี
เลขทะเบียนไม่ต้องสนใจมาก|Don't worry much about the plate|ทะเบียน,ไม่สำคัญ
ทะเบียนนำโชค|A lucky plate|ทะเบียน,โชค
ได้เลขเด็ดจากทะเบียนรถ|A lucky number from the plate|ทะเบียน,เลขเด็ด
เลขไมล์ตอนรับรถเป็นมงคล|The odometer at delivery is a lucky number|เลขมงคล,ไมล์
ป้ายทะเบียนจังหวัดบ้านเกิด|Plate from your home province|ทะเบียน,จังหวัด
เปลี่ยนทะเบียนแล้วดวงดีขึ้น|New plate, better luck|ทะเบียน,ความเชื่อ
ทะเบียนเก่ามีเรื่องไม่ดี|The old plate carries bad history|ทะเบียน,ระวัง
ทะเบียนสวยช่วยขายต่อ|A nice plate helps resale|ทะเบียน,ขายต่อ
เลขทะเบียนถูกกับเบอร์โทร|Plate matches your phone number|ทะเบียน,เลขมงคล
ไม่ควรจ่ายแพงเพื่อทะเบียน|Don't overpay for a plate|ทะเบียน,คุ้มค่า
ใช้ทะเบียนเลขธรรมดาก็ดี|An ordinary plate is fine|ทะเบียน,พอดี
ดูเลขทะเบียนตามวันเกิด|Pick a plate by your birth day|ทะเบียน,วันเกิด
เลขศาสตร์ทะเบียนเสริมการงาน|Plate numerology helps your work|ทะเบียน,การงาน
""")

cat('ฤกษ์และความเชื่อ', """
ดูฤกษ์ออกรถ|Find an auspicious delivery time|ฤกษ์,ความเชื่อ
ออกรถวันพฤหัสดี|Thursday is good for delivery|ฤกษ์,ความเชื่อ
ออกรถวันศุกร์ดี|Friday is good for delivery|ฤกษ์,ความเชื่อ
เลี่ยงออกรถวันเสาร์|Avoid Saturday for delivery|ฤกษ์,ความเชื่อ
เลี่ยงออกรถวันอังคาร|Avoid Tuesday for delivery|ฤกษ์,ความเชื่อ
ออกรถตรงวันเกิด|Take delivery on your birthday|ฤกษ์,ความเชื่อ
เจิมรถก่อนใช้|Have the car blessed first|เจิมรถ,ความเชื่อ
ให้พระเจิมรถ|Have a monk bless the car|เจิมรถ,ความเชื่อ
ผูกผ้าสามสีหน้ารถ|Tie three-colour cloth on the front|ผ้าสามสี,ความเชื่อ
ไหว้แม่ย่านางรถ|Pay respect to the car's guardian spirit|แม่ย่านาง,ความเชื่อ
ถวายพวงมาลัยแม่ย่านาง|Offer a garland to the guardian spirit|แม่ย่านาง,ความเชื่อ
ไหว้เจ้าที่ก่อนนำรถเข้าบ้าน|Pay respect to the house spirit first|เจ้าที่,ความเชื่อ
ทำบุญก่อนรับรถ|Make merit before delivery|ทำบุญ,ความเชื่อ
ขับไปไหว้พระวัดแรก|Drive to a temple first|ไหว้พระ,ความเชื่อ
ห้อยพระในรถ|Hang an amulet in the car|พระเครื่อง,ความเชื่อ
ติดยันต์ในรถ|Put a yantra in the car|ยันต์,ความเชื่อ
วางพระบนคอนโซล|Place a Buddha image on the dash|พระพุทธรูป,ความเชื่อ
พวงมาลัยหน้ารถเสริมสิริมงคล|A garland on the mirror brings blessings|พวงมาลัย,ความเชื่อ
ไหว้พระประจำวันเกิดก่อนขับ|Pray to your birth-day Buddha before driving|ไหว้พระ,ความเชื่อ
สวดคาถาก่อนออกเดินทาง|Say a protective chant before trips|คาถา,ความเชื่อ
ปีชงระวังรถใหม่|Clash year: careful with a new car|ปีชง,ความเชื่อ
แก้ชงก่อนออกรถ|Ward off the clash year before buying|ปีชง,ความเชื่อ
ดวงมีโชคเรื่องยานพาหนะ|Your chart is lucky with vehicles|ดวง,ยานพาหนะ
ดวงต้องระวังยานพาหนะ|Your chart warns about vehicles|ดวง,ระวัง
ราหูเข้า ระวังรถ|Rahu is on you: careful with cars|ราหู,ระวัง
ดาวพฤหัสหนุนได้รถ|Jupiter helps you get a car|ดาวพฤหัส,ได้รถ
รถคันนี้ถูกชะตา|This car is your fate|ถูกชะตา,ความเชื่อ
รถคันนี้ไม่ถูกชะตา|This car isn't meant for you|ไม่ถูกชะตา,ความเชื่อ
รถเก่าเคยมีอุบัติเหตุร้ายแรง|The old car had a serious accident|ประวัติรถ,ความเชื่อ
ขอขมาแม่ย่านางรถเก่า|Ask forgiveness of the old car's spirit|แม่ย่านาง,ความเชื่อ
ฝันว่าได้รถใหม่|You dream of a new car|ฝัน,ความเชื่อ
ฝันว่ารถหาย|You dream your car is lost|ฝัน,ความเชื่อ
รถคันแรกนำโชค|Your first car brings luck|โชค,ความเชื่อ
ได้รถจากการชิงโชค|You win a car in a draw|โชค,โชคลาภ
ได้รถเป็นของขวัญ|You get a car as a gift|ของขวัญ,โชคลาภ
ตั้งชื่อรถเสริมดวง|Give the car a lucky name|ชื่อรถ,ความเชื่อ
ทิศจอดรถหน้าบ้านดี|Good direction for parking at home|ทิศ,ฮวงจุ้ย
จอดรถหันหัวออกดี|Park facing out|ทิศ,ฮวงจุ้ย
โรงจอดรถฮวงจุ้ยดี|Good feng shui for the garage|ฮวงจุ้ย,บ้าน
ทำบุญให้แม่ย่านางทุกปี|Make merit for the car spirit every year|แม่ย่านาง,ความเชื่อ
อย่าเชื่อฤกษ์จนลืมตรวจสภาพ|Don't let rituals replace an inspection|ความเชื่อ,สติ
มูแล้วต้องขับดีด้วย|Blessings still need careful driving|ความเชื่อ,ความปลอดภัย
""")

cat('ความปลอดภัยและการใช้งาน', """
ขับปลอดภัยตลอดปี|Safe driving all year|ความปลอดภัย,ดี
ระวังอุบัติเหตุช่วงแรก|Careful in the first months|อุบัติเหตุ,ระวัง
ระวังขับเร็ว|Watch your speed|ขับเร็ว,ระวัง
ระวังขับกลางคืน|Careful driving at night|กลางคืน,ระวัง
ระวังเดินทางไกลช่วงเทศกาล|Careful on long holiday trips|เดินทาง,ระวัง
ระวังรถถูกขโมย|Watch for car theft|ขโมย,ระวัง
ระวังของในรถหาย|Watch for theft from the car|ขโมย,ระวัง
ระวังน้ำท่วมจอดรถ|Watch for flooding where you park|น้ำท่วม,ระวัง
ระวังรถถูกขูด|Watch for scratches|รอยขีดข่วน,ระวัง
ขับทางไกลได้สบาย|Comfortable on long drives|เดินทาง,ดี
เหมาะใช้ในเมือง|Suits city driving|ในเมือง,เหมาะ
เหมาะขับต่างจังหวัด|Suits country driving|ต่างจังหวัด,เหมาะ
เหมาะกับครอบครัว|Suits the family|ครอบครัว,เหมาะ
เหมาะกับการทำงาน|Suits your work|การงาน,เหมาะ
ใช้รถทำมาหากินได้|Use it to earn a living|การงาน,รายได้
ปล่อยรถให้เช่าได้รายได้|Renting it out earns money|รายได้,เช่า
ขับรับส่งผู้โดยสารได้|Good for ride-hailing|รายได้,การงาน
คนในบ้านได้ใช้ด้วย|The whole family uses it|ครอบครัว,ใช้งาน
ให้คนอื่นยืมรถไม่ดี|Don't lend the car out|ยืมรถ,ระวัง
ติดกล้องหน้ารถไว้|Fit a dash cam|กล้อง,ความปลอดภัย
พักให้พอก่อนขับไกล|Rest well before long drives|พักผ่อน,ความปลอดภัย
คาดเข็มขัดทุกที่นั่ง|Belt up in every seat|เข็มขัด,ความปลอดภัย
ใช้คาร์ซีตสำหรับเด็ก|Use a child seat|เด็ก,ความปลอดภัย
ไม่ขับหลังดื่ม|Never drive after drinking|ความปลอดภัย,ข้อห้าม
ไม่เล่นมือถือขณะขับ|No phone while driving|ความปลอดภัย,ข้อห้าม
ที่จอดรถที่บ้านพอ|Enough parking at home|ที่จอด,ดี
ที่จอดรถไม่พอ|Not enough parking|ที่จอด,ปัญหา
ที่ชาร์จรถไฟฟ้าสะดวก|Easy EV charging|ชาร์จ,รถไฟฟ้า
ที่ชาร์จรถไฟฟ้าไม่สะดวก|EV charging is a hassle|ชาร์จ,รถไฟฟ้า
ขับรถคู่ใจไปเที่ยวบ่อย|Many road trips ahead|เดินทาง,ความสุข
""")

cat('ค่าใช้จ่ายหลังซื้อ', """
ค่าประกันไม่แพง|Insurance is affordable|ประกัน,ค่าใช้จ่าย
ค่าประกันแพง|Insurance is expensive|ประกัน,ค่าใช้จ่าย
ทำประกันชั้นหนึ่งดีกว่า|First-class insurance is better|ประกัน,แนะนำ
ประกันชั้นสองบวกก็พอ|Class 2+ is enough|ประกัน,พอดี
เคลมประกันง่าย|Claims are easy|ประกัน,เคลม
เคลมประกันยุ่งยาก|Claims are a hassle|ประกัน,เคลม
ค่าบำรุงรักษาต่ำ|Low upkeep|บำรุงรักษา,ประหยัด
ค่าบำรุงรักษาสูง|High upkeep|บำรุงรักษา,แพง
ค่าซ่อมไม่คาดคิด|Unexpected repair bill|ซ่อม,ระวัง
เข้าศูนย์ตามระยะ|Service on schedule|บำรุงรักษา,ดี
อู่นอกดีกว่าศูนย์|An independent garage is better|อู่,ทางเลือก
หาอู่ประจำที่ไว้ใจได้|Find a garage you trust|อู่,ดี
ค่าน้ำมันกินงบ|Fuel eats the budget|น้ำมัน,ค่าใช้จ่าย
ค่าไฟชาร์จถูกกว่าน้ำมัน|Charging is cheaper than fuel|รถไฟฟ้า,ประหยัด
ค่าทางด่วนเพิ่มขึ้น|More spent on tolls|ค่าใช้จ่าย,ทางด่วน
ค่าที่จอดรถแพง|Parking is expensive|ที่จอด,ค่าใช้จ่าย
ภาษีรถประจำปีไม่แพง|Annual road tax is low|ภาษี,ค่าใช้จ่าย
ต้องเปลี่ยนแบตเตอรี่เร็วๆ นี้|The battery needs replacing soon|แบตเตอรี่,ซ่อม
ต้องเปลี่ยนยางเร็วๆ นี้|The tyres need replacing soon|ยาง,ซ่อม
ค่าแต่งรถบานปลาย|Mods get out of hand|แต่งรถ,ระวัง
แต่งรถพอดีๆ ก็สวย|A few tasteful mods are enough|แต่งรถ,พอดี
ติดฟิล์มกรองแสงดี|Good window tint|ฟิล์ม,ดี
เคลือบสีรถคุ้ม|Paint protection is worth it|ดูแล,คุ้มค่า
เก็บเงินสำรองค่ารถไว้|Keep a car fund|เงินสำรอง,การเงิน
ค่าใช้จ่ายรวมเกินคาด|Total cost is more than expected|ค่าใช้จ่าย,ระวัง
ค่าใช้จ่ายรวมพอดีกับรายได้|Total cost fits your income|ค่าใช้จ่าย,ดี
ได้ส่วนลดเข้าศูนย์ฟรี|Free servicing included|บำรุงรักษา,โปรโมชัน
ประกันรถหมดอย่าลืมต่อ|Don't let insurance lapse|ประกัน,ระวัง
พ.ร.บ. ต้องต่อให้ทัน|Renew compulsory insurance on time|พ.ร.บ.,ระวัง
""")

cat('ขายรถเก่าและเทิร์น', """
ขายรถเก่าได้ราคาดี|The old car sells well|ขายรถ,ดี
ขายรถเก่าไม่ออก|The old car won't sell|ขายรถ,ยาก
เทิร์นรถเก่าคุ้ม|Trading in is worth it|เทิร์น,คุ้มค่า
ขายเองได้ราคากว่าเทิร์น|Selling it yourself pays more|ขายรถ,ทางเลือก
เก็บรถเก่าไว้ใช้คู่กัน|Keep the old car too|รถเดิม,เก็บไว้
ยกรถเก่าให้คนในบ้าน|Give the old car to family|รถเดิม,ครอบครัว
รถเก่ามีความหลังดี|The old car holds good memories|รถเดิม,ความทรงจำ
ปล่อยรถเก่าไปเพื่อเริ่มใหม่|Let the old car go and start fresh|รถเดิม,เริ่มใหม่
ผู้ซื้อรถเก่าจริงใจ|An honest buyer for the old car|ขายรถ,ผู้ซื้อ
ระวังผู้ซื้อเบี้ยวเงิน|Watch for a buyer who won't pay|ขายรถ,ระวัง
โอนรถเก่าให้เรียบร้อย|Finish transferring the old car|โอน,เอกสาร
ปิดไฟแนนซ์คันเก่าก่อน|Pay off the old loan first|ไฟแนนซ์,รถเดิม
ราคาเทิร์นต่ำกว่าคาด|Trade-in offer is low|เทิร์น,ราคา
ราคาเทิร์นสูงกว่าคาด|Trade-in offer is high|เทิร์น,ราคา
ขายรถตอนนี้ได้จังหวะ|Now is the time to sell|ขายรถ,จังหวะ
รอขายรถทีหลังดีกว่า|Better to sell later|ขายรถ,ควรรอ
ไม่ต้องมีรถสองคัน|You don't need two cars|รถเดิม,พอดี
มีรถสองคันสะดวกขึ้น|Two cars make life easier|รถเดิม,สะดวก
รถเก่าถึงเวลาปลดระวาง|The old car's time is up|รถเดิม,เปลี่ยน
ซ่อมรถเก่าคุ้มกว่าซื้อใหม่|Fixing the old car beats buying|ซ่อม,คุ้มค่า
""")

cat('ผลลัพธ์หลังได้รถ', """
ได้รถแล้วชีวิตสะดวกขึ้น|Life gets easier with the car|ผลลัพธ์,สะดวก
ได้รถแล้วงานดีขึ้น|Work improves with the car|ผลลัพธ์,การงาน
ได้รถแล้วเงินตึง|Money gets tight after buying|ผลลัพธ์,การเงิน
ได้รถแล้วครอบครัวมีความสุข|The family is happier|ผลลัพธ์,ครอบครัว
ได้รถแล้วความรักดี|Love life improves|ผลลัพธ์,ความรัก
ได้รถแล้วเดินทางบ่อยขึ้น|You travel more|ผลลัพธ์,เดินทาง
ได้รถแล้วมีโชคลาภ|Good fortune comes with the car|ผลลัพธ์,โชคลาภ
รถพาไปเจอโอกาสใหม่|The car leads to new chances|ผลลัพธ์,โอกาส
รถคันนี้อยู่ด้วยกันนาน|You'll keep this car a long time|ผลลัพธ์,ยาวนาน
เปลี่ยนใจขายเร็วกว่าที่คิด|You'll sell it sooner than planned|ผลลัพธ์,เปลี่ยนใจ
พอใจกับรถคันนี้มาก|Very happy with this car|ผลลัพธ์,พอใจ
เสียดายที่ไม่ได้เลือกคันอื่น|You'll wish you'd chosen another|ผลลัพธ์,เสียดาย
รถคันนี้เป็นที่อิจฉา|People will envy this car|ผลลัพธ์,ภาพลักษณ์
รถเสริมภาพลักษณ์|The car lifts your image|ผลลัพธ์,ภาพลักษณ์
อย่าซื้อรถเพื่ออวด|Don't buy a car to show off|ใจ,ระวัง
ซื้อเพราะจำเป็นจริง|Buy because you truly need it|ใจ,จำเป็น
ซื้อเพราะอยากให้รางวัลตัวเอง|Buy it as a reward to yourself|ใจ,รางวัล
คนรอบตัวช่วยเลือกได้ดี|People around you help you choose well|คนรอบตัว,ดี
คนรอบตัวค้าน|People around you object|คนรอบตัว,ค้าน
คู่ครองเห็นด้วย|Your partner agrees|ความรัก,เห็นด้วย
คู่ครองไม่เห็นด้วย|Your partner disagrees|ความรัก,ไม่เห็นด้วย
พ่อแม่สนับสนุน|Your parents back you|ครอบครัว,สนับสนุน
ได้รถคันในฝัน|You get your dream car|ผลลัพธ์,ความฝัน
ยังไม่ใช่รถคันในฝัน|Not your dream car yet|ผลลัพธ์,ความฝัน
รถคันต่อไปจะดีกว่านี้|Your next car will be better|อนาคต,ดีขึ้น
""")

open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
names = [l.split('|')[0] for l in out if not l.startswith('#')]
import collections
d = [n for n, c in collections.Counter(names).items() if c > 1]
print(len(names), 'dups', d)
for l in out:
    if l.startswith('#'): print(l)
