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
        style="width: 300px;height: 200px" 
        autoplay loop>
    </dotlottie-wc>
    """

intro =  f"""
            <h3>
            Introduktion
            </h3>

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

            {animation2}

        """

erfarings_html = """
<style>

.accordion {
    width: 100%;
}

.accordion-item {
    margin-bottom: 12px;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
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
            <h3>
            Erfaring
            </h3>

            {erfarings_html}
            """

komp = f"""            
            <h3>
            Kompetencer
            </h3>

            <div class="skills">
                <span class="skill">Nyhedsproduktion</span>
                <span class="skill">Nysgerrig og idérig</span>
                <span class="skill">Engagerende digital formidling</span>
                <span class="skill">Kreativ og positiv arbejdshest</span>
                <span class="skill">Webscraping og databearbejdning</span>
                <span class="skill">Struktureret og analytisk</span>
            </div>
            """

portfolio = f"""
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 0;
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
}}

.skill {{
    background: #E8F5E9;
    border: 1px solid #C8E6C9;
    border-radius: 999px;
    padding: 8px 14px;
    font-size: 0.95rem;
    font-weight: 600;
    text-align: center;
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
                {komp}
            </div>

        </div>

        <div>

            <div class="section reveal">
                {erfaring}
            </div>

        </div>

    </div>

    <div style="height:100px;"></div>

    <div class="reveal">
        {animation}
    </div>

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
