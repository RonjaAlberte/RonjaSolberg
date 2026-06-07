### Module for html-coding

import streamlit as st
import streamlit.components.v1 as components

animation = """
    <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.9.14/dist/dotlottie-wc.js" type="module"></script>

    <dotlottie-wc
        src="https://lottie.host/d501ef9d-8709-42c2-a5db-ffb55df465d6/aN4XxDbMgX.lottie"
        style="width:600px;height:600px;"
        autoplay
        loop>
    </dotlottie-wc>
    """

animation2 = """
    <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.9.14/dist/dotlottie-wc.js" type="module"></script>
                             
    <dotlottie-wc 
        src="https://lottie.host/6b3d8d8d-3810-4029-a282-ee1afc8d0fa0/cFocZa642X.lottie" 
        style="width: 300px;height: 300px;transform: translateX(200px) rotate(30deg);" 
        autoplay loop>
    </dotlottie-wc>
    """

intro =  f"""
            <h2>
            Introduktion
            </h2>

            <p>
            Med min tidligere erfaring som nyhedsjournalist i DR, og mine digitale
            kompetencer som Data Scientist, er jeg sikker på, at jeg er den oplagte
            nye kollega på DR Nyheders digitale redaktion.
            </p>

            <p>
            Jeg brænder nemlig for at gøre komplekse historier inddragende og
            letforståelige for <i>alle</i> danskere; og har oven i hatten erfaring med at
            gøre det gennem engagerende digitale og visuelle virkemidler.
            </p>

            <p>
            Det er min overbevisning at en af grundpillerne for et velfungerende demokrati, 
            er gjort af en befolkning, der forstår verden omkring dem - også det og dem, 
            der ligger langt fra deres egen hverdag. 
            </p>

            <p>
            Derfor vil det glæde mig at være med til at skabe historier, der fanger danskerne, 
            og som kan være med til at bygge bro over de grøfter, 
            der kun er blevet dybere mellem os over de seneste år. 
            </p>
        """

ansogning1 = """
            <p>
                Der er blevet langt imellem danskerne. 
                Unge mænd og kvinder driver længere fra hinanden på det politiske spektrum, 
                uligheden mellem by og land vokser, og en mere polariseret retorik har fundet indtog i Danmark. 
                Derfor er der brug for journalistik, der giver perspektiv i en verden, 
                som alt for ofte fremstilles sort/hvid. Historier, der hjælper brugerne med at forstå 
                de store sammenhænge frem for blot at følge nyhedsstrømmen. 
            </p>
            """
samling = f"""
        <style>
            .samling {{
                font-size: 0.95rem;
                font-weight: 500;
                text-align: center;
            }}
        </style>
        <div class="samling">
            <p> Et <i>samlingspunkt.</i></p>
        </div>"""
samling2 = """<p>
                Det er DR for rigtig mange danskere, og derfor søger jeg stillingen som journalist i Digitale Nyhedsprodukter.
            </p>"""
ansogning2 = """
            <p>
                Jeg brænder nemlig for at gøre komplekse historier forståelige, engagerende og relevante for brugerne. 
                Det gælder både i den daglige nyhedsdækning og i de større projekter, hvor der er mulighed 
                for at gå et spadestik dybere. Som journalist på DR Syd og DR Bornholm lærte jeg at finde de vinkler 
                og historier, der betyder noget for mennesker, og som jourhavende udviklede jeg evnen til at 
                træffe selvstændige redaktionelle beslutninger og bevare overblikket, når tempoet er højt.
            </p>
            <p>
                Samtidig har jeg bevidst søgt mod krydsfeltet mellem journalistik, data og digitale fortælleformer. 
                Med en kandidat i Data Science fra Syddansk Universitet har jeg opbygget kompetencer inden for dataanalyse, 
                visualisering, programmering og maskinlæring, som jeg ser som journalistiske værktøjer snarere end 
                tekniske discipliner. For mig handler data ikke om teknologi for teknologiens skyld, 
                men om at finde nye historier, nye vinkler og nye måder at skabe forståelse på.
            </p>
            """

ansogning3 = """
            <p>
                Senest har jeg arbejdet som datajournalist hos Gravercentret, hvor jeg udviklede et projekt, 
                der automatisk indsamlede data fra kommuner og regioner, opsummerede politiske dagsordener 
                ved hjælp af en egenudviklet sprogmodel og gjorde materialet tilgængeligt gennem interaktive værktøjer. 
                Projektet udsprang af mit speciale og blev til med ambitionen om at styrke den undersøgende journalistik
                i lokale medier. Det lærte mig ikke alene at arbejde undersøgende og databaseret, 
                men også at tænke journalistik som produkter og brugeroplevelser frem for alene artikler.
            </p>
            <p>
                Netop den tankegang tiltaler mig ved Digitale Nyhedsprodukter. 
                Jeg motiveres af at udvikle journalistik, der udnytter digitale muligheder til at gøre 
                komplekse historier lettere at forstå og mere interessante at engagere sig i. 
                Jeg synes, nogle af de mest spændende journalistiske produkter opstår, når stærk formidling, 
                data, design og teknologi arbejder sammen om at besvare spørgsmålet: 
                Hvad har brugerne egentlig brug for at forstå?
            </p>
            """

ansogning4 ="""
            <p>
                Som gæsteunderviser og eksaminator på DMJX har jeg samtidig fået styrket min evne til at 
                identificere den gode historie og den stærke vinkel. Gennem vejledning af studerende og vurdering
                af journalistiske projekter har jeg trænet mit blik for, hvad der gør journalistik relevant, 
                vedkommende og nyskabende. Det er en erfaring, jeg vil tage med mig i mit kommende arbejde.
            </p>
            <p>
                Jeg søger stillingen, fordi den kombinerer alt det, der motiverer mig mest: 
                journalistik med samfundsmæssig betydning, digitale fortælleformer og ambitionen om konstant 
                at udvikle nye måder at formidle de store historier på. Jeg vil gerne være med til at skabe de produkter, 
                der får brugerne til at stoppe op, blive klogere og se verden i et større perspektiv.
            </p>
            <p>
                Jeg ser frem til muligheden for at uddybe min motivation og fortælle mere om, 
                hvordan jeg kan bidrage til Digitale Nyhedsprodukter.
            </p>
            <p>Med venlig hilsen</p>
            <p><i>Ronja Solberg</i></p>
            """

erfarings_html = """
<style>

.accordion {
    width: 100%;
}

.accordion-item {
    margin-bottom: 12px;
    border: 1px solid #C8E6C9;
    border-radius: 15px;
    overflow: hidden;
    background: white;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

.accordion input {
    display: none;
}

.accordion label {
    display: block;
    padding: 18px 22px;
    cursor: pointer;
    font-weight: 600;
    font-size: 1rem;
    transition: background-color .2s ease;
}

.accordion label:hover {
    background: #f7f7f7;
}

.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height .4s ease;
    padding: 0 22px;
}

.accordion input:checked + label + .accordion-content {
    max-height: 800px;
    padding-bottom: 22px;
}

.job-title {
    font-size: 1.1rem;
    font-weight: 700;
}

.company {
    color: #666;
    font-style: italic;
    margin-bottom: 12px;
}

.date {
    float: right;
    color: #888;
    font-weight: 400;
}

ul {
    padding-left: 20px;
}

</style>

<div class="accordion">

    <div class="accordion-item">

        <input type="radio" name="experience" id="exp1" checked>

        <label for="exp1">
            Gæsteunderviser og eksaminator
            <span class="date">feb 2026 – nu</span>
        </label>

        <div class="accordion-content">

            <div class="company">
                Danmarks Medie- og Journalisthøjskole
            </div>

            <p>
            I forårssemestret har jeg stået for en datavisualiserings-workshop i Python
            for de internationale kandidatstuderende på Erasmus Mundus-forløbet.
            </p>

            <p>
            Her lærte jeg de studerende at lave interaktive grafikker, der engagerer og
            vedrører modtageren, og har derudover givet eksamensvejledning og karakterer
            for deres afsluttende journalistiske projekter.
            </p>

        </div>

    </div>

    <div class="accordion-item">

        <input type="radio" name="experience" id="exp2">

        <label for="exp2">
            Datajournalist
            <span class="date">aug 2025 – jan 2026</span>
        </label>

        <div class="accordion-content">

            <div class="company">
                Gravercentret – Danmarks Center for Undersøgende Journalistik
            </div>

            <p>
            For Gravercentret lavede jeg en researchpakke baseret på mit specialeprojekt, der bestod af:
            </p>

            <ul>
                <li>Automatisk scraping af alle kommuner og regioners hjemmesider</li>
                <li>Udvikling af en sprogmodel til referater af politiske møder og dagsordener</li>
                <li>Opsætning af en avanceret database med over 1 million datapunkter</li>
                <li>Design og udvikling af en interaktiv hjemmeside</li>
            </ul>

            <p>
            Løsningen gør det muligt for journalister selv at filtrere, dykke ned i og finde historier i dataet.
            </p>

        </div>

    </div>

    <div class="accordion-item">

        <input type="radio" name="experience" id="exp3">

        <label for="exp3">
            Studentermedhjælper, Data Science
            <span class="date">aug 2024 – jul 2025</span>
        </label>

        <div class="accordion-content">

            <div class="company">
                Strong Productions & Blu
            </div>

            <p>
            Som studentermedhjælper i programudviklingen havde jeg ansvar for at etablere en databaseret tilgang til idéudviklingen.
            Det var en helt ny 'pioner'-stilling, hvor jeg ene mand havde ansvaret og friheden til at indføre de analyser, der ville
            give mening for idéudviklingen.
            </p>

            <p>
            Det lykkedes mig at indføre flere gode analyseredskaber, blandt andre:
            </p>

            <ul>
                <li>Trendanalyser</li>
                <li>Sentimentanalyser</li>
                <li>Segmentanalyser</li>
                <li>Analyse af influencers reach og engagement</li>
                <li>Automatisering af seertalsanalyser gennem webscraping og automatiseret databearbejdning</li>
            </ul>

        </div>

    </div>

    <div class="accordion-item">

        <input type="radio" name="experience" id="exp4">

        <label for="exp4">
            Journalist
            <span class="date">aug 2019 – dec 2022</span>
        </label>

        <div class="accordion-content">

            <div class="company">
                DR – Danmarks Radio
            </div>

            <p>
            Med tre og et halvt års erfaring som journalist på henholdsvis DR Syd og DR Bornholm,
            har jeg suget til mig af kompetencer indenfor journalistisk formidling i form af bl.a. 
            reportage og kort, effektiv og præcis nyhedsformidling.
            </p>

            <p>
            Derudover har jeg som jourhavende finpudset mine evner til at tage selvstændige redaktionelle beslutninger
            og holde det forkromede overblik over redaktionens opgaver,
            når ansvaret for den samlede tilstedeværelse i radioen og på dr.dk lå hos mig.
            </p>

        </div>

    </div>

</div>
"""

erfaring = f"""            
            <h2>
            Erfaring
            </h2>

            {erfarings_html}
            """

komp = f"""            
            <h2>
            Kompetencer
            </h2>

            <div class="skills">
                <span class="skill">Nyhedsproduktion</span>
                <span class="skill">Nysgerrig og initiativrig</span>
                <span class="skill">Engagerende digital formidling</span>
                <span class="skill">Struktureret og analytisk</span>
                <span class="skill">Webscraping og databearbejdning</span>
                <span class="skill">Kreativ og positiv arbejdshest</span>
            </div>
            """

cand = f"""
    <style>
    .udd {{
        text-align: center;
    }}
    .project {{
        font-weight: 400;
        color: #888;
    }}

    </style>
    <h2>
    Uddannelse og udmærkelser
    </h2>

    <div class="skills">
        <span class="udd"><h3>Cand.Scient i Data Science</h3>
            <div class="company">
                Syddansk Universitet
            </div>
            <div class="company">
                2023 – 2026
            </div>

            <p>
            Med min kandidat i Data Science har jeg fået gode redskaber til min datajournalistiske værktøjskasse. 
            Udover de vanlige fag i blandt andet Python, interaktiv visualisering og maskinlæring, 
            tog jeg et valgfag i Undersøgende Journalistik fra cand.public.
            </p>

            <p>
            Jeg afsluttede min kandidat med 12 for mit speciale.
            </p>
            <div class="project"> 
                <i>Fra Dagsorden til Deadline: AI i Lokaljournalistik</i>
            </div>
        </span>

        <span class="udd"><h3>Journalist</h3>
            <div class="company">
                Danmarks Medie- og Journalisthøjskole
            </div>
            <div class="company">
                2017 – 2021
            </div>

            <p>
            I løbet af uddannelsen tog jeg valgfag i datajournalistik og EU-politik. 
            Det var her jeg blev bidt af de mange muligheder og historier, der gemmer sig i OSINT.
            Samtidig fik jeg en stor interesse for al den politik, der ikke foregår på Christiansborg, 
            men ude i kommunerne, regionerne og i EU. 
            </p>

            <p>
            Jeg afsluttede med 10 for mit bachelorprojekt.
            </p>
            <div class="project"> 
                <i>Den sidste indianer: Fiskemangel i de indre danske farvande</i>
            </div>
        </span>

    </div>
    """

talent = """
    <div class="talent">
        <span class="udd"><h3>Talent Fellow</h3>
        <div class="company">
            Den Fynske Bladfond
        </div>
        <p>
        Min specialemakker Jonatan May og jeg blev udnævnt til Talent Fellows for vores specialeprojekt.
        Vi modtog et legat og muligheden for at sparre med journalister i branchen, der gav feedback
        på vores prototype, foruden et styrket netværk og adgang til MediaTech Festival. 
    </div>
    """

portfolio = f"""
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 0;
    margin-top: 20px;
}}

.wrapper {{
    max-width: 1200px;
    margin: auto;
}}

.grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
}}

.divider {{
    content: "";
    display: block;
    width: 900px;
    height: 2px;
    margin: 10px auto 0 auto;
    margin-bottom: 0px;
    background: #C8E6C9;
    border-radius: 999px;
}}

h2 {{
    text-align: center;
    margin-bottom: 20px;
}}

h3 {{
    text-align: center;
    margin-bottom: 10px;
}}

h3::after {{
    content: "";
    display: block;
    width: 60px;
    height: 3px;
    margin: 10px auto 0 auto;
    margin-bottom: 25px;
    background: #C8E6C9;
    border-radius: 999px;
}}

.reveal {{
    opacity: 0;
    transform: translateY(40px);
    transition: all 1.5s ease;
}}

.reveal.visible {{
    opacity: 1;
    transform: translateY(0);
}}

.section {{
    margin-bottom: 50px;
}}

.skills {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 50px;
}}

.skill {{
    background: #A5D6A7;
    border: 1px solid #A8D5BA;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    border-radius: 999px;
    padding: 12px 14px;
    font-size: 0.95rem;
    font-weight: 500;
    text-align: center;
    color: white;
}}

.midt {{
    text-align: center;
    margin-left: 200px;
    margin-right: 200px;
    margin-bottom: 50px;
}}

.talent {{
    text-align: center;
    margin-left: 300px;
    margin-right: 300px;
    margin-top: 20px;
    margin-bottom: 20px;
}}

.kontakt-boks {{
    position: sticky;
    text-align: center;
    font-size: 0.9rem;
    line-height: 1.7;
}}

.kontakt-boks a {{
    color: inherit;
    text-decoration: none;
}}

.kontakt-boks a:hover {{
    text-decoration: underline;
}}

@media (max-width: 900px) {{
    .grid {{
        grid-template-columns: 1fr;
    }}
}}
</style>

<script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.9.14/dist/dotlottie-wc.js" type="module"></script>

<div class="wrapper">

    <div class="grid">

        <div>

            <div class="section reveal">
                {intro}
            </div>
            <div class="section reveal">
                {animation2}
            </div>
        </div>

        <div>

            <div class="section reveal">
                {erfaring}
            </div>
            
        </div>
    </div>

    <div class="reveal">
        <div style="height:30px;"></div>
        <h3>Min motivation</h3>
    </div>

    <div class="midt reveal">
        {ansogning1}
    </div>
    <div class="midt reveal">
        {samling}
    </div>
    <div class="midt reveal">
        {samling2}
    </div>

    <div class="grid">

        <div>

            <div class="section reveal">
                {ansogning2}
            </div>
            <div class="section reveal">
                {ansogning3}
            </div>

        </div>

        <div>
            <div class="section reveal">
                {ansogning4}
            </div>
            <div class="section reveal">
                {komp}
            </div>
            
        </div>
    </div>

    <div class="reveal">
        <span class="divider"></span>
    </div>

    <div style="height:10px;"></div>

    <div class="reveal">
        {cand}
    </div>

    <div class="reveal">
        <div style="height:20px;"></div>
        {talent}
        <div style="height:40px;"></div>
        <span class="divider"></span>
        <div style="height:10px;"></div>
        </div>
    </div>

</div>

<div class="kontakt-boks">
    <strong>Kontakt</strong><br>
    <a href="mailto:ronjaalberte@gmail.com">ronjaalberte@gmail.com</a><br>
    <a href="tel:+4560601102">+45 6060 1102</a><br>
    <a href="https://www.linkedin.com/in/ronjasolberg/" target="_blank">
        linkedin.com/in/ronjasolberg
    </a>
</div>

<script>
const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
        if (entry.isIntersecting) {{
            entry.target.classList.add('visible');
        }}
    }});
}}, {{
    threshold: 0.15
}});

document.querySelectorAll('.reveal').forEach(el => {{
    observer.observe(el);
}});
</script>
"""

def header():
    components.html(
        """
        <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            overflow-x: hidden;
        }

        .container {
            position: relative;
            width: 100%;
            height: 700px;
        }

        .animation {
            position: absolute;
            inset: 0;
            z-index: 1;
        }

        .hero-content {
            position: relative;
            z-index: 2;
            text-align: center;
            padding-top: 180px;
            color: black;
        }

        .hero-content h2 {
            font-size: 2.4rem;
            margin-bottom: 10px;
        }

        .hero-content h4 {
            font-size: 1.2rem;
            font-weight: 400;
        }

        .reveal {
            opacity: 0;
            transform: translateY(40px);
            transition: all 1.2s ease;
            max-width: 800px;
            margin: 100px auto;
            font-size: 1.2rem;
            line-height: 1.8;
            color: #222;
            padding: 0 20px;
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
        </style>

        <div class="container">

            <div class="animation">
                <script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.9.14/dist/dotlottie-wc.js" type="module"></script>

                <dotlottie-wc
                    src="https://lottie.host/d501ef9d-8709-42c2-a5db-ffb55df465d6/aN4XxDbMgX.lottie"
                    style="width:100%;height:100%;"
                    autoplay
                    loop>
                </dotlottie-wc>
            </div>

            <div class="hero-content">
                <h2>
                    Kreativ datajournalist med blik for den interaktive &
                    engagerende historie
                </h2>

                <h3><i>Ronja Solberg</i></h3>
            </div>

        </div>
        """,
        height=682,
    )

def revealer(text,height):
    components.html(
        f"""
        <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
        }}

        .spacer {{
            height: 30px;
        }}

        .reveal {{
            opacity: 0;
            animation: fadeInUp 2s ease forwards;
            animation-delay: 0s;
            max-width: 800px;
            margin: auto;
            font-size: 1rem;
            line-height: 1.7;
        }}

        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(40px);
            }}

            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        </style>

        <div class="spacer"></div>

        <div class="reveal">
            {text}
        </div>
        """,
        height=height,
    )
