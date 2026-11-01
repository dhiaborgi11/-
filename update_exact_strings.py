# -*- coding: utf-8 -*-
with open('/home/dhiaborgi/.gemini/antigravity/scratch/karl-marx-website/build_full_site.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Hero Title to include full exact "كارل ماركس (1818 – 1883)"
code = code.replace(
    '<h1 class="text-4xl sm:text-5xl xl:text-6xl font-black text-[#f0ece1] tracking-tight leading-tight mb-3">\n                كارل ماركس\n              </h1>',
    '<h1 class="text-4xl sm:text-5xl xl:text-6xl font-black text-[#f0ece1] tracking-tight leading-tight mb-3">\n                كارل ماركس (1818 – 1883)\n              </h1>'
)

# 2. Update Featured Quote in parchment box to include exact verbatim string:
# «إن الفلاسفة لم يفعلوا غير تفسير العالم بطرق مختلفة، ولكن المهم هو تغييره.» — أطروحات حول فيورباخ (1845)
old_quote_block = """              <!-- Quote Content -->
              <blockquote class="font-amiri text-xl sm:text-2xl font-bold leading-relaxed text-[#2a2217] my-3 text-center">
                «إن الفلاسفة لم يفعلوا غير تفسير العالم بطرق مختلفة، ولكن المهم هو تغييره.»
              </blockquote>

              <!-- Citation Source -->
              <div class="text-center font-bold text-xs text-[#6b5a45] mt-3 pt-2 border-t border-[#9e8156]/30">
                — أطروحات حول فيورباخ (1845)
              </div>"""

new_quote_block = """              <!-- Quote Content -->
              <blockquote class="font-amiri text-xl sm:text-2xl font-bold leading-relaxed text-[#2a2217] my-3 text-center">
                «إن الفلاسفة لم يفعلوا غير تفسير العالم بطرق مختلفة، ولكن المهم هو تغييره.» — أطروحات حول فيورباخ (1845)
              </blockquote>

              <!-- Citation Source -->
              <div class="text-center font-bold text-xs text-[#6b5a45] mt-3 pt-2 border-t border-[#9e8156]/30">
                — الأطروحة الحادية عشرة من أطروحات حول فيورباخ (1845)
              </div>"""

code = code.replace(old_quote_block, new_quote_block)

# 3. Update Book 2 title to exact string:
# رأس المال: نقد الاقتصاد السياسي (المجلد الأول 1867)
code = code.replace(
    '<h3 class="text-2xl font-bold text-[#f0ece1] mb-2 font-cairo">رأس المال: نقد الاقتصاد السياسي</h3>',
    '<h3 class="text-2xl font-bold text-[#f0ece1] mb-2 font-cairo">رأس المال: نقد الاقتصاد السياسي (المجلد الأول 1867)</h3>'
)

# 4. Check timeline exact strings:
# "1818: ولادته في مدينة ترير بألمانيا."
code = code.replace('<p class="text-sm text-[#cbd5e1]">\n                    ولادته في مدينة ترير بألمانيا.\n                  </p>', '<p class="text-sm text-[#cbd5e1]">\n                    <strong>1818:</strong> ولادته في مدينة ترير بألمانيا.\n                  </p>')
code = code.replace('<p class="text-sm text-[#cbd5e1]">\n                    نيل الدكتوراه في الفلسفة من جامعة يينا.\n                  </p>', '<p class="text-sm text-[#cbd5e1]">\n                    <strong>1841:</strong> نيل الدكتوراه في الفلسفة من جامعة يينا.\n                  </p>')
code = code.replace('<p class="text-sm text-[#cbd5e1]">\n                    اللقاء الأول بفريدريك إنجلز في باريس.\n                  </p>', '<p class="text-sm text-[#cbd5e1]">\n                    <strong>1844:</strong> اللقاء الأول بفريدريك إنجلز في باريس.\n                  </p>')
code = code.replace('<p class="text-sm text-[#cbd5e1]">\n                    نشر «البيان الشيوعي» متزامناً مع الثورات العمالية.\n                  </p>', '<p class="text-sm text-[#cbd5e1]">\n                    <strong>1848:</strong> نشر «البيان الشيوعي» متزامناً مع الثورات العمالية.\n                  </p>')
code = code.replace('<p class="text-sm text-[#cbd5e1]">\n                    لجوؤه واستقراره النهائي في لندن.\n                  </p>', '<p class="text-sm text-[#cbd5e1]">\n                    <strong>1849:</strong> لجوؤه واستقراره النهائي في لندن.\n                  </p>')
code = code.replace('<p class="text-sm text-[#cbd5e1]">\n                    المساهمة في تأسيس جمعية الشغيلة العالمية (الأممية الأولى).\n                  </p>', '<p class="text-sm text-[#cbd5e1]">\n                    <strong>1864:</strong> المساهمة في تأسيس جمعية الشغيلة العالمية (الأممية الأولى).\n                  </p>')
code = code.replace('<p class="text-sm text-[#cbd5e1]">\n                    نشر المجلد الأول من «رأس المال».\n                  </p>', '<p class="text-sm text-[#cbd5e1]">\n                    <strong>1867:</strong> نشر المجلد الأول من «رأس المال».\n                  </p>')
code = code.replace('<p class="text-sm text-[#cbd5e1]">\n                    وفاته في لندن ودفنه في مقبرة هايغيت.\n                  </p>', '<p class="text-sm text-[#cbd5e1]">\n                    <strong>1883:</strong> وفاته في لندن ودفنه في مقبرة هايغيت.\n                  </p>')

with open('/home/dhiaborgi/.gemini/antigravity/scratch/karl-marx-website/build_full_site.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_full_site.py with exact strings")
