# Al-Driven Development - 30-Day Challenge Task-3

Prepared by: Muhammad Sufiyan  
Class Slot: Friday 6:00 PM to 9:00 PM  
Instructor: Sir Hamzah Syed

---

★ PART A – Research Questions (Short Answers)

1. What new improvements were introduced in Gemini 3.0?

Gemini 3.0 mein advanced natural language understanding, improved context handling, aur better reasoning capabilities introduce ki gayi hain. Yeh version multimodal inputs ko efficiently samajhne aur creative responses dene mein behtari lata hai. Performance aur latency mein bhi improvement hui hai.

2. How does Gemini 3.0 improve coding & automation workflows?

Gemini 3.0 developers ko advanced code generation, debugging support, aur integration with automation tools provide karta hai. Is se development faster, accurate, aur zyada productive hoti hai.

3. How does Gemini 3.0 improve multimodal understanding?

Gemini 3.0 text ke alawa images, audio, aur video inputs ko bhi samajh kar unka context analyze karta hai, jis se AI responses zyada accurate aur context-aware bante hain.

4. Name any two developer tools introduced with Gemini 3.0.

- Gemini CLI (Command-line interface for model management)  
- AutoGen SDK (AI agent development toolkit)

---

★ PART B – Practical Task (Screenshot Required)

Task Steps:

1. Gemini CLI mein /model command se Gemini 3.0 model update karen.

2. Example command:

model set gemini-3-pro-preview

3. Update hone ke baad model ka naam show ho raha ho, uska screenshot len.

4. CLI software update nahi karna, sirf model update karna hai.

---

★ Additional Research – Gemini CLI Model System & Auto Fallback

Gemini CLI ka backend model system dynamic hai aur koi aik model permanently fixed nahi hota. Yeh system:

- Sabse pehle user ke task complexity aur access level ke mutabiq highest capability model (jaise gemini-3-pro-preview) ko use karne ki koshish karta hai.

- Agar wo model unavailable ho ya slow response de, to automatic fallback karke lower-tier models (jaise gemini-2.5-pro ya gemini-1.5-flash) par shift hota hai.

Is mechanism ki wajah se AI service smooth, reliable, aur uninterrupted rehti hai.

CLI interface pe aapko multiple model options dikhte hain, lekin backend dynamically un models mein se best available model choose karta hai.

---

Kya hum sirf ek model fix kar sakte hain?

Jee haan aur nahi, dono tarah ke jawab hain:

*Technically:*  
Aap CLI mein command dekar ek specific model set kar sakte hain, jaise:

model set gemini-3-pro-preview

Ya

model set gemini-2.5-flash

Is se CLI koshish karega ke wohi model use ho.

*Lekin backend constraints ke wajah se:*  
Agar wo model aapke account ya system pe temporarily available nahi hai, to system fallback kar sakta hai lower-tier model par bina aapko error dikhaye.

Iska matlab:  
Aap officially ek model prefer kar sakte hain, lekin backend infrastructure kabhi kabhi fallback karne par majboor hota hai.

---

Summary:

| Point                  | Explanation                          |
|------------------------|------------------------------------|
| Model set kar sakte hain| CLI me specific model select kar sakte hain |
| Backend may fallback ho sakta hai | System access ya availability ke mutabiq fallback hota hai |
| Permanent fix karna mushkil | Infrastructure aur permission ke wajah se |

---

Iska matlab ye hai ke aap apni preference de sakte hain, lekin system ki taraf se fallback automatic rahega.


---

Aap ab is content ko apni repo ke Task-3/README.md file me paste karen aur commit & push kar den.

Agar chahiye to main commit message bhi suggest kar doon.