# -*- coding: utf-8 -*-
with open('/home/dhiaborgi/.gemini/antigravity/scratch/karl-marx-website/build_full_site.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the timeline items to contain exact strings:
timeline_pairs = [
    ("1818", "ولادته في مدينة ترير بألمانيا."),
    ("1841", "نيل الدكتوراه في الفلسفة من جامعة يينا."),
    ("1844", "اللقاء الأول بفريدريك إنجلز في باريس."),
    ("1848", "نشر «البيان الشيوعي» متزامناً مع الثورات العمالية."),
    ("1849", "لجوؤه واستقراره النهائي في لندن."),
    ("1864", "المساهمة في تأسيس جمعية الشغيلة العالمية (الأممية الأولى)."),
    ("1867", "نشر المجلد الأول من «رأس المال»."),
    ("1883", "وفاته في لندن ودفنه في مقبرة هايغيت.")
]

for year, desc in timeline_pairs:
    # Target whatever is currently in <p class="text-sm text-[#cbd5e1]">
    target_str = f"<strong>{year}:</strong> {desc}"
    replacement_str = f"{year}: {desc}"
    code = code.replace(target_str, replacement_str)

with open('/home/dhiaborgi/.gemini/antigravity/scratch/karl-marx-website/build_full_site.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated timeline items in build_full_site.py")
