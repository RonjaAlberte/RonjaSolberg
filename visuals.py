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
        style="width: 600px;height: 300px" 
        autoplay loop>
    </dotlottie-wc>
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
            animation-delay: 3s;
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

intro =  """
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
        """

erfaring = """            
            <h3>
            Erfaring
            </h3>
            """

def erfaringsbokse():
    with st.expander("**Gæsteunderviser og eksaminator** | DMJX | feb 2026 – nu"):
        st.markdown("""
##### Gæsteunderviser og eksaminator
*Danmarks Medie- og Journalisthøjskole*
                    
I forårssemestret har jeg stået for en datavisualiserings-workshop i Python for de internationale kandidatstuderende på Erasmus Mundusforløbet. 
                    
Her lærte jeg de studerende at lave interaktive grafikker, der engagerer og vedrører modtageren, og har derudover givet 
eksamensvejledning og karakterer for deres afsluttende journalistiske projekter."""
                    )
    st.markdown("")
    with st.expander("**Datajournalist** | Gravercentret | aug 2025 – jan 2026"):
        st.markdown("""
##### Datajournalist
*Gravercentret - Danmarks Center for Undersøgende Journalistik*
                    
Hos Gravercentret lavede jeg en researchpakke for dem. Det var en udvidelse af mit specialeprojekt, der bestod af:

- Automatisk scraping af alle kommuner og regioners hjemmesider
- Udvikling af en sprogmodel, der gav korte referater af politiske møder og dagsordener
- Opsætning af en avanceret database
- Design og udvikling af en hjemmeside med interaktive moduler

Løsningen gør det muligt for journalister selv at filtrere, dykke ned i og finde historier i dataet.
""")
    st.markdown("")
    with st.expander("**Studentermedhjælper** | Fremantle | aug 2024 – jul 2025"):
        st.markdown("""
##### Studentermedhjælper, Data Science
*Strong Productions & Blu*

Som studentermedhjælper i programudviklingen havde jeg ansvar for at etablere en databaseret tilgang til idéudviklingen.

Det indførte jeg blandt andet gennem:

- Statistiske analyser af trends
- Sentimentanalyser
- Segmentanalyser
- Analyse af influencers reach og engagement
- Automatisering af tilbagevendende arbejdsopgaver

Arbejdet gav redaktionen et mere datadrevet grundlag for udvikling af nye formater.
""")
    st.markdown("")
    with st.expander("**Journalist** | DR | aug 2019 – dec 2022"):
        st.markdown("""
##### Journalist
*DR – Danmarks Radio*

Med tre og et halvt års erfaring som journalist på henholdsvis DR Syd og DR Bornholm, har jeg suget til mig af kompetencer indenfor journalistisk formidling i form af bl.a. reportage og kort, effektiv og præcis nyhedsformidling. 

Derudover har jeg som jourhavende finpudset mine evner til at tage selvstændige redaktionelle beslutninger og holde det forkromede overblik over redaktionens opgaver, når ansvaret for den samlede tilstedeværelse i radioen og på dr.dk lå hos mig.
""")