import streamlit as st
import random
import math
import time

# -------------------------------
# MATEMATICA
# -------------------------------
def fact(n: int) -> int:
    return math.factorial(n)

def C(n: int, k: int) -> int:
    return fact(n) // (fact(k) * fact(n - k))

def C_rep(n: int, k: int) -> int:
    # combinazioni con ripetizione: C(n+k-1, k)
    return C(n + k - 1, k)

def D(n: int, k: int) -> int:
    return fact(n) // fact(n - k)

# -------------------------------
# ESERCIZI (più "narrativi" e vari)
# Ogni esercizio definisce:
# testo, n, k, ordine, rip, tipo, spiegazione
# -------------------------------

LEVELS = [
    {
        "name": "Livello 1 — Principiante (Permutazioni)",
        "goal": 6,
        "desc": "Qui ti alleni a riconoscere quando stai semplicemente ORDINANDO tutti gli elementi (n = k).",
        "pool": [
            {
                "testo": "🎭 Teatro: 6 amici devono sedersi in 6 posti in fila. In quanti modi diversi possono sedersi?",
                "n": 6, "k": 6, "ordine": True, "rip": False,
                "tipo": "Permutazioni", "spiegazione": "Stai ordinando tutte le persone (n=k), quindi n!."
            },
            {
                "testo": "📚 Libreria: 5 libri diversi vanno messi in fila su uno scaffale. Quanti ordini possibili?",
                "n": 5, "k": 5, "ordine": True, "rip": False,
                "tipo": "Permutazioni", "spiegazione": "Stai ordinando tutti e 5 i libri: 5!."
            },
            {
                "testo": "🧍‍♂️🧍‍♀️ Foto di gruppo: 7 persone si mettono in fila per una foto. Quanti ordini possibili?",
                "n": 7, "k": 7, "ordine": True, "rip": False,
                "tipo": "Permutazioni", "spiegazione": "È un ordinamento completo: 7!."
            },
            {
                "testo": "🏁 Gara: 4 corridori diversi si dispongono su 4 corsie (una per corsia). In quanti modi?",
                "n": 4, "k": 4, "ordine": True, "rip": False,
                "tipo": "Permutazioni", "spiegazione": "Assegnare 4 persone a 4 posizioni distinte: 4!."
            },
            {
                "testo": "🍽️ Cena: 8 persone e 8 posti numerati. Quanti modi di sedersi?",
                "n": 8, "k": 8, "ordine": True, "rip": False,
                "tipo": "Permutazioni", "spiegazione": "Posti distinti e tutte le persone: 8!."
            },
            {
                "testo": "🎲 Carte: 6 carte diverse vengono messe in fila. Quante sequenze?",
                "n": 6, "k": 6, "ordine": True, "rip": False,
                "tipo": "Permutazioni", "spiegazione": "Ordine completo senza ripetizione: 6!."
            },
        ],
    },
    {
        "name": "Livello 2 — Intermedio (Disposizioni senza ripetizione)",
        "goal": 7,
        "desc": "Ora l’ordine conta, ma NON stai usando tutti gli elementi (n ≠ k).",
        "pool": [
            {
                "testo": "🏢 Azienda: tra 50 persone scegli Presidente, Vicepresidente e Segretario. In quanti modi?",
                "n": 50, "k": 3, "ordine": True, "rip": False,
                "tipo": "Disposizioni", "spiegazione": "Ruoli diversi ⇒ ordine conta, niente ripetizioni ⇒ D(n,k)."
            },
            {
                "testo": "🥇 Podio: in una gara con 10 partecipanti, quanti modi per assegnare oro-argento-bronzo?",
                "n": 10, "k": 3, "ordine": True, "rip": False,
                "tipo": "Disposizioni", "spiegazione": "Podio ordinato (1°,2°,3°) senza ripetizione ⇒ D(10,3)."
            },
            {
                "testo": "🎤 Talent: tra 12 concorrenti scegli 4 finalisti in ordine di uscita sul palco. Quanti modi?",
                "n": 12, "k": 4, "ordine": True, "rip": False,
                "tipo": "Disposizioni", "spiegazione": "Ordine di uscita importa, nessuno ripetuto ⇒ D(12,4)."
            },
            {
                "testo": "🔑 Codice: hai 9 simboli diversi e devi creare un codice di 3 simboli senza ripetere. Quanti codici?",
                "n": 9, "k": 3, "ordine": True, "rip": False,
                "tipo": "Disposizioni", "spiegazione": "Sequenza ordinata, senza ripetizioni ⇒ D(9,3)."
            },
            {
                "testo": "🏫 Scuola: tra 20 studenti scegli Capitano e Vicecapitano (ruoli diversi). Quanti modi?",
                "n": 20, "k": 2, "ordine": True, "rip": False,
                "tipo": "Disposizioni", "spiegazione": "Capitano/Vice sono ruoli distinti ⇒ ordine conta ⇒ D(20,2)."
            },
            {
                "testo": "🎮 Team: da 15 giocatori scegli 5 per un lineup, e conta l’ordine di schieramento. Quanti modi?",
                "n": 15, "k": 5, "ordine": True, "rip": False,
                "tipo": "Disposizioni", "spiegazione": "Ordine importante e nessuno ripetuto ⇒ D(15,5)."
            },
            {
                "testo": "🧪 Laboratorio: scegli 3 provette diverse da 11 e le metti in ordine su un supporto (1-2-3). Quanti modi?",
                "n": 11, "k": 3, "ordine": True, "rip": False,
                "tipo": "Disposizioni", "spiegazione": "Posizioni diverse ⇒ ordine conta ⇒ D(11,3)."
            },
        ],
    },
    {
        "name": "Livello 3 — Pro (Combinazioni senza ripetizione)",
        "goal": 7,
        "desc": "Qui scegli gruppi: l’ordine NON conta e non puoi ripetere.",
        "pool": [
            {
                "testo": "🤝 12 amici si stringono la mano. Quante strette di mano totali?",
                "n": 12, "k": 2, "ordine": False, "rip": False,
                "tipo": "Combinazioni", "spiegazione": "Una coppia A-B è uguale a B-A ⇒ combinazioni C(n,2)."
            },
            {
                "testo": "🧑‍🤝‍🧑 Gruppo: in una classe di 20 studenti scegli 3 rappresentanti (tutti uguali come ruolo). Quanti modi?",
                "n": 20, "k": 3, "ordine": False, "rip": False,
                "tipo": "Combinazioni", "spiegazione": "Stai scegliendo un gruppo di 3, ordine irrilevante ⇒ C(20,3)."
            },
            {
                "testo": "🍕 Cena: devi scegliere 4 amici su 10 per uscire (nessun ruolo diverso). Quanti gruppi possibili?",
                "n": 10, "k": 4, "ordine": False, "rip": False,
                "tipo": "Combinazioni", "spiegazione": "Gruppi senza ordine ⇒ C(10,4)."
            },
            {
                "testo": "🎟️ Biglietti: scegli 2 vincitori su 15 (due persone diverse). Quanti modi?",
                "n": 15, "k": 2, "ordine": False, "rip": False,
                "tipo": "Combinazioni", "spiegazione": "Scelta di 2 senza ordine ⇒ C(15,2)."
            },
            {
                "testo": "📦 Magazzino: scegli 5 scatole diverse tra 13 da spedire. Quanti modi?",
                "n": 13, "k": 5, "ordine": False, "rip": False,
                "tipo": "Combinazioni", "spiegazione": "Scelta di un insieme, non una sequenza ⇒ C(13,5)."
            },
            {
                "testo": "⚽ Torneo: scegli 3 squadre su 9 per un mini-girone. Quanti possibili gironi?",
                "n": 9, "k": 3, "ordine": False, "rip": False,
                "tipo": "Combinazioni", "spiegazione": "Girone = gruppo di squadre, ordine irrilevante ⇒ C(9,3)."
            },
            {
                "testo": "🎬 Cast: scegli 6 attori su 14 per un progetto (tutti stesso ruolo). Quanti cast possibili?",
                "n": 14, "k": 6, "ordine": False, "rip": False,
                "tipo": "Combinazioni", "spiegazione": "È una selezione senza ordine ⇒ C(14,6)."
            },
        ],
    },
    {
        "name": "Livello 4 — Boss (Ripetizioni)",
        "goal": 8,
        "desc": "Qui entrano le ripetizioni: password, scelte uguali, caramelle uguali…",
        "pool": [
            {
                "testo": "🔐 Password: una password è composta da 4 cifre (0–9), e le cifre possono ripetersi. Quante password?",
                "n": 10, "k": 4, "ordine": True, "rip": True,
                "tipo": "Disposizioni con ripetizione", "spiegazione": "Ogni posizione ha 10 scelte indipendenti ⇒ 10^4."
            },
            {
                "testo": "🎰 Codice: scegli 6 simboli da 5 possibili, e puoi ripetere simboli. Conta l’ordine. Quante sequenze?",
                "n": 5, "k": 6, "ordine": True, "rip": True,
                "tipo": "Disposizioni con ripetizione", "spiegazione": "Sequenza ordinata con ripetizione ⇒ n^k."
            },
            {
                "testo": "🍬 Caramelle: 10 gusti, scegli 3 caramelle (puoi prendere più volte lo stesso gusto). Quanti modi?",
                "n": 10, "k": 3, "ordine": False, "rip": True,
                "tipo": "Combinazioni con ripetizione", "spiegazione": "Scelta senza ordine con ripetizione ⇒ C(n+k-1,k)."
            },
            {
                "testo": "🍕 Pizze: menu da 10 pizze, ne ordini 2 e puoi prenderne due uguali. Quanti ordini possibili?",
                "n": 10, "k": 2, "ordine": False, "rip": True,
                "tipo": "Combinazioni con ripetizione", "spiegazione": "Ordine non conta (margherita+diavola = diavola+margherita) e puoi ripetere ⇒ C(11,2)."
            },
            {
                "testo": "🎁 Regali: 6 tipi di gadget, prendi 4 gadget totali (anche uguali). Quanti modi di scegliere?",
                "n": 6, "k": 4, "ordine": False, "rip": True,
                "tipo": "Combinazioni con ripetizione", "spiegazione": "Scelta con ripetizione, senza ordine ⇒ C(6+4-1,4)=C(9,4)."
            },
            {
                "testo": "🔢 PIN: PIN di 3 cifre (0–9), cifre ripetibili. Quanti PIN?",
                "n": 10, "k": 3, "ordine": True, "rip": True,
                "tipo": "Disposizioni con ripetizione", "spiegazione": "Ordine conta e ripetizioni ammesse ⇒ 10^3."
            },
            {
                "testo": "🍦 Gelato: 5 gusti, scegli 3 palline (anche stesso gusto). Quanti modi?",
                "n": 5, "k": 3, "ordine": False, "rip": True,
                "tipo": "Combinazioni con ripetizione", "spiegazione": "Senza ordine, con ripetizione ⇒ C(5+3-1,3)=C(7,3)."
            },
            {
                "testo": "🎼 Note: scegli 4 note da 7, e l’ordine della melodia conta, note ripetibili. Quante melodie?",
                "n": 7, "k": 4, "ordine": True, "rip": True,
                "tipo": "Disposizioni con ripetizione", "spiegazione": "Ogni posizione può essere una delle 7 note ⇒ 7^4."
            },
        ],
    },
]

# -------------------------------
# LOGICA: calcolo formula + risultato
# -------------------------------
def compute_formula(ex):
    n, k = ex["n"], ex["k"]
    if ex["ordine"] and not ex["rip"]:
        if n == k:
            res = fact(n)
            name = "Permutazioni"
            formula = f"{n}! = {res}"
            pretty = f"n! con n={n}"
        else:
            res = D(n, k)
            name = "Disposizioni semplici"
            formula = f"D({n},{k}) = {n}!/({n}-{k})! = {res}"
            pretty = f"D(n,k) con n={n}, k={k}"
        return name, pretty, formula, res

    if ex["ordine"] and ex["rip"]:
        res = n ** k
        name = "Disposizioni con ripetizione"
        formula = f"{n}^{k} = {res}"
        pretty = f"n^k con n={n}, k={k}"
        return name, pretty, formula, res

    if (not ex["ordine"]) and (not ex["rip"]):
        res = C(n, k)
        name = "Combinazioni semplici"
        formula = f"C({n},{k}) = {n}!/({k}!({n}-{k})!) = {res}"
        pretty = f"C(n,k) con n={n}, k={k}"
        return name, pretty, formula, res

    # no ordine, sì rip
    res = C_rep(n, k)
    name = "Combinazioni con ripetizione"
    formula = f"C({n}+{k}-1,{k}) = C({n+k-1},{k}) = {res}"
    pretty = f"C(n+k-1,k) con n={n}, k={k}"
    return name, pretty, formula, res


# -------------------------------
# STATO GIOCO (session_state)
# -------------------------------
def reset_run():
    st.session_state.lives = 3
    st.session_state.score = 0
    st.session_state.streak = 0
    st.session_state.level_idx = 0
    st.session_state.level_done = 0
    st.session_state.used_ids = set()
    st.session_state.screen = "level_start"
    st.session_state.last_feedback = None
    st.session_state.last_answer_correct = None

def pick_question(level_idx):
    pool = LEVELS[level_idx]["pool"]

    # id deterministico: indice nel pool
    candidates = [i for i in range(len(pool)) if (level_idx, i) not in st.session_state.used_ids]
    if not candidates:
        # se finiti, reset solo i used di quel livello
        st.session_state.used_ids = {x for x in st.session_state.used_ids if x[0] != level_idx}
        candidates = list(range(len(pool)))

    i = random.choice(candidates)
    st.session_state.used_ids.add((level_idx, i))
    return pool[i], i

if "screen" not in st.session_state:
    reset_run()

# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="Combinatorio Game", page_icon="🎮", layout="centered")

# HUD
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"**❤️ Vite:** {'❤️'*st.session_state.lives}{'🖤'*(3-st.session_state.lives)}")
with col2:
    st.markdown(f"**⭐ Punti:** {st.session_state.score}")
with col3:
    st.markdown(f"**🔥 Streak:** {st.session_state.streak}")

st.divider()

# GAME OVER
if st.session_state.lives <= 0:
    st.error("💀 GAME OVER — Hai finito i cuori!")
    st.write(f"Punteggio finale: **{st.session_state.score}**")
    if st.button("🔁 Ricomincia"):
        reset_run()
        st.rerun()
    st.stop()

# Schermata Level Start
if st.session_state.screen == "level_start":
    lvl = LEVELS[st.session_state.level_idx]
    st.title("🎮 Calcolo Combinatorio — Game Mode")
    st.subheader(lvl["name"])
    st.write(lvl["desc"])
    st.info(f"Obiettivo livello: **{lvl['goal']}** domande completate.")
    if st.button("🚀 Inizia livello"):
        st.session_state.current_q, st.session_state.current_q_id = pick_question(st.session_state.level_idx)
        st.session_state.screen = "question"
        st.session_state.last_feedback = None
        st.session_state.last_answer_correct = None
        st.rerun()

# Schermata domanda
if st.session_state.screen == "question":
    lvl = LEVELS[st.session_state.level_idx]
    goal = lvl["goal"]

    # progress
    progress = st.session_state.level_done / goal
    st.progress(progress, text=f"Progresso livello: {st.session_state.level_done}/{goal}")

    st.subheader("📌 Missione")
    st.write(st.session_state.current_q["testo"])

    ordine = st.radio("L’ordine conta?", ["SI", "NO"], horizontal=True, key="ordine_choice")
    rip = st.radio("Ripetizioni ammesse?", ["SI", "NO"], horizontal=True, key="rip_choice")

    c1, c2 = st.columns(2)
    with c1:
        confirm = st.button("✅ Conferma")
    with c2:
        st.button("🔁 Reset partita", on_click=reset_run)

    if confirm:
        ex = st.session_state.current_q
        ordine_bool = (ordine == "SI")
        rip_bool = (rip == "SI")

        correct = (ordine_bool == ex["ordine"]) and (rip_bool == ex["rip"])

        name, pretty, formula, res = compute_formula(ex)

        # punteggio + vite
        if correct:
            st.session_state.score += 100
            st.session_state.streak += 1
            # streak bonus
            if st.session_state.streak == 2:
                st.session_state.score += 50
            elif st.session_state.streak == 3:
                st.session_state.score += 100
            elif st.session_state.streak == 5:
                st.session_state.score += 250
        else:
            st.session_state.lives -= 1
            st.session_state.streak = 0
            st.session_state.score = max(0, st.session_state.score - 50)

        st.session_state.level_done += 1

        st.session_state.last_answer_correct = correct
        st.session_state.last_feedback = {
            "tipo": ex["tipo"],
            "name": name,
            "pretty": pretty,
            "formula": formula,
            "spiegazione": ex["spiegazione"],
            "corretto": correct
        }

        st.session_state.screen = "feedback"
        st.rerun()

# Schermata feedback
if st.session_state.screen == "feedback":
    lvl = LEVELS[st.session_state.level_idx]
    goal = lvl["goal"]
    fb = st.session_state.last_feedback

    st.subheader("🧾 Risultato round")

    if fb["corretto"]:
        st.success("✅ Corretto! +100 punti")
    else:
        st.error("❌ Sbagliato! -1 ❤️ e -50 punti")

    st.write(f"**Caso riconosciuto:** {fb['name']}")
    st.write(f"**Formula (idea):** {fb['pretty']}")
    st.code(fb["formula"])
    st.write(f"**Perché:** {fb['spiegazione']}")

    # fine livello?
    if st.session_state.level_done >= goal:
        st.divider()
        st.success(f"🏁 Livello completato: {lvl['name']}")
        st.write(f"Precisione/score attuale: **{st.session_state.score}** punti")
        if st.session_state.level_idx < len(LEVELS) - 1:
            if st.button("➡️ Vai al livello successivo"):
                st.session_state.level_idx += 1
                st.session_state.level_done = 0
                st.session_state.screen = "level_start"
                st.session_state.last_feedback = None
                st.session_state.last_answer_correct = None
                st.rerun()
        else:
            st.balloons()
            st.success("🏆 Hai finito tutti i livelli! Sei il Boss del combinatorio.")
            if st.button("🔁 Ricomincia dal livello 1"):
                reset_run()
                st.rerun()
    else:
        if st.button("➡️ Prossima missione"):
            st.session_state.current_q, st.session_state.current_q_id = pick_question(st.session_state.level_idx)
            st.session_state.screen = "question"
            st.session_state.last_feedback = None
            st.session_state.last_answer_correct = None
            st.rerun()