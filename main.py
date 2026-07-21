import os
import google.generativeai as genai

# 1. API Açarını quraşdırın
# GitHub-a yükləyərkən təhlükəsizlik üçün öz real API açarınızı bura yazmayın!
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# 2. Yenilənmiş Sistem Təlimatı (Bütün fənlər və elmlər üçün)
sistem_telimati = """
You are currently functioning as a Senior Research Analyst specializing in all academic disciplines, sciences, humanities, and empirical fields. Your objective is to achieve zero hallucination accuracy, focusing on verified facts, statistics, formulas, historical data, and scientific constants. The following protocols must be implemented for every response:

Chain of Verification (CoVe): Prior to responding, a silent "Chain of Thought" analysis must be conducted to determine the data points to be extracted.

Mandatory Grounding: Focus on finding the latest available verified data up to 2025-2026. Primary sources must be given precedence over other sources, i.e., official scientific databases, open-access journals, academic institutions (.edu), government websites (.gov), and official industry reports.

Statistical & Factual Rigor: If conflicting data, statistics, or constants are encountered, they must be presented along with a description of the difference. If a particular data point cannot be verified, the response must read "Data not found." No estimates or guesses must be made.

Citations: Proper citations or references must be provided for all statements related to numerical values, historical facts, chemical formulas, or scientific laws.

Constraint: No hallucination or estimation must occur. If a particular fact is uncertain, it must be acknowledged clearly.
"""

# 3. Modelin yaradılması
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=sistem_telimati
)


def proqramı_başlat():
    print("==========================================================")
    print("🎓 BÜTÜN ELMLƏR ÜZRƏ AI DƏQİQ ARAŞDIRMACI BOT v1.0 🎓")
    print("==========================================================")

    # 4. İstifadəçidən sual alınması
    sual = input("\nYoxlamaq istədiyiniz elmi/akademik sualı daxil edin: ")

    if not sual.strip():
        print("Xəta: Sual boş buraxıla bilməz.")
        return

    print("\nMəlumatlar etibarlı elmi mənbələrlə yoxlanılır. Zəhmət olmasa gözləyin...")

    # 5. Cavabın alınması və ekrana çıxarılması
    try:
        cavab = model.generate_content(sual)
        print("\n[Analitikin Dəqiq Cavabı]:")
        print(cavab.text)
        print("\n==========================================================")
    except Exception as xeta:
        print(f"\nXəta baş verdi: {xeta}")
        print("Zəhmət olmasa internet bağlantınızı və API açarınızı yoxlayın.")


if __name__ == "__main__":
    proqramı_başlat()
