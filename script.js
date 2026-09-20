// Project Case Studies Database
const projectDatabase = {
    chefling: {
        logo: "assets/projects/chefling.png",
        tag: "Startup • GTM Strategy",
        title: "Chefling Ramen Launch GTM",
        about: "Chefling is an emerging Indian food-tech startup dedicated to democratizing global cuisines through innovative DIY meal kits. The brand gained national recognition after securing ₹40 lakhs on Shark Tank India Season 3. Riding the wave of Korean culture popularity and rising demand for convenient international food, Chefling is entering the fast-growing instant ramen market.",
        approach: [
            "Market Research: Mapped market size, consumer behavior, and competitor benchmarks (e.g., Samyang, Master Chow).",
            "Segmentation: Identified key customer segments based on price sensitivity and flavor preferences.",
            "Marketing Roadmap: Designed a 3-phase strategy using community building, influencers, and experiential marketing.",
            "Distribution & UX: Proposed an online-to-offline model and highlighted UX friction points in DIY onboarding."
        ],
        impact: [
            { val: "12%", desc: "Higher CTR through optimized push notification campaigns" },
            { val: "Lower CAC", desc: "Achieved through cohort-based audience targeting" },
            { val: "7% Increase", desc: "Estimated rise in conversion rate with onboarding UI improvements" }
        ]
    },
    ketto: {
        logo: "assets/projects/ketto.png",
        tag: "Corporate • Product Research",
        title: "Ketto Crowdfunding Attitudinal Study",
        about: "Ketto is a leading Indian crowdfunding platform launched in 2012 to help individuals and organizations raise funds for medical needs, education, social causes, and emergencies. With a zero-platform-fee model, it has raised millions. The Impact Project conducted detailed research to map donor sentiments and product viability.",
        approach: [
            "Primary Research: Deployed surveys to assess donor preferences, trust factors, and willingness to pay.",
            "Audience Mapping: Mapped pricing sensitivity and affordability gaps across demographic factors.",
            "Marketing Strategy: Created influencer-driven and content-led marketing frameworks to build credibility.",
            "Data Interpretation: Proposed tiered product models and gender-personalized offerings based on attitudinal data."
        ],
        impact: [
            { val: "46%", desc: "Of users preferred pricing under ₹5,000, establishing affordable tiers" },
            { val: "60%", desc: "Discovered platform via social channels, validating influencer-led approach" },
            { val: "30%", desc: "Lower resistance in high-weight segments by offering trial/EMI models" }
        ]
    },
    renteagle: {
        logo: "assets/projects/renteagle.png",
        tag: "Startup • Market Analysis",
        title: "RentEagle Scaling Strategy",
        about: "RentEagle is a Delhi-based rental platform revolutionizing access to lifestyle essentials like furniture, electronics, books, apparel, and accessories for urban Indians. RentEagle empowers customers with the flexibility to rent, subscribe, or purchase items based on evolving needs.",
        approach: [
            "Competitor Analysis: Conducted an in-depth competitor analysis of key players in the rental industry to understand market positioning.",
            "Best Practice Benchmarking: Benchmarked successful practices and identified actionable strategies to integrate into operations.",
            "Digital Marketing: Evaluated digital marketing tools to enhance website traffic and boost customer engagement.",
            "Vertical Feasibility: Analyzed the event management business segment, including its cost structure and revenue potential."
        ],
        impact: [
            { val: "3 Models", desc: "Supply chain models identified based on competitor best practices" },
            { val: "40%", desc: "Increase in LinkedIn post engagement through content marketing strategies" },
            { val: "5+ Clients", desc: "Potential clients identified for the event management segment feasibility" }
        ]
    },
    sadagamaya: {
        logo: "assets/projects/sadagamaya.png",
        tag: "NGO • Social Strategy",
        title: "Sadagamaya Community Expansion",
        about: "Sadagamaya is a non-profit organization committed to improving the lives of underprivileged communities by organizing blood donation camps, food distribution, medical equipment charity, and conducting free health checkups.",
        approach: [
            "Behavioral Research: Conducted comprehensive research on individual behavioral patterns to improve participation in donation drives.",
            "Community Outreach: Initiated collaborations with educational institutions and hospitals for checkup campaigns.",
            "Financial Allocation Model: Developed a dynamic model and automated Excel sheet to handle expenses and revenue updates.",
            "Branding and Tech: Designed a comprehensive website mockup to support marketing and outreach strategies."
        ],
        impact: [
            { val: "Psychology", desc: "Identified donor psychology and beliefs to build trust" },
            { val: "Multi-Platform", desc: "Proposed online digital strategies to enhance donation rates" },
            { val: "Excel Model", desc: "Created dynamic spreadsheet models for secure financial planning" }
        ]
    },
    dor: {
        logo: "assets/projects/dor.png",
        tag: "NGO • Capital Scaling",
        title: "DOR Foundation Funding Roadmap",
        about: "DOR Foundation (Development, Opportunity, Resilience) is committed to empowering communities and driving sustainable change. They focus on inclusive growth in education, healthcare, women's empowerment, and climate resilience through community-led solutions.",
        approach: [
            "Fundraising Strategy: Evaluated funding options among government grants, corporate CSR, and crowdfunding.",
            "Talent Acquisition: Set in place a volunteer acquisition model to build a skilled and dedicated team.",
            "Revenue Model: Explored and developed a subscription-based model for the NGO to maintain working capital.",
            "Engagement Planning: Designed donor acquisition campaigns and long-term retention frameworks."
        ],
        impact: [
            { val: "10 Lakhs", desc: "Government grant assisted to expand operational needs" },
            { val: "45%", desc: "Revenue increase achieved via strategic partnership with Building Dreams" },
            { val: "75%", desc: "Enhanced LinkedIn engagement through close-worked content campaigns" }
        ]
    },
    oneinme: {
        logo: "assets/projects/1inme.png",
        tag: "NGO • Global Research",
        title: "1in.me International Benchmarking",
        about: "1in.me is designed to celebrate individuality and unlock personal growth. Through a variety of carefully crafted tools, resources, and a supportive community, self-expression is encouraged, connecting changemakers.",
        approach: [
            "Market Research: Surveyed and benchmarked potential target markets around the globe based on impact metrics.",
            "Competitive Mapping: Segmented markets by geography, demographics, and competitive landscape.",
            "Marketing Design: Structured organic strategies for email, influencer, YouTube, podcasting, and cause-marketing.",
            "Roadmap Planning: Developed a timeline for campaigns, contests, and community-led events."
        ],
        impact: [
            { val: "5-7% Lower", desc: "Pricing structured compared to market leaders using data-driven models" },
            { val: "4 Countries", desc: "Analyzed Brazil, UK, India, and Sweden market size indicators for entry" },
            { val: "Audience Target", desc: "Completed comprehensive target audience profiles for local alignment" }
        ]
    }
};

document.addEventListener("DOMContentLoaded", () => {
    // 1. Sticky Navigation Scroll Effect
    const header = document.getElementById("mainHeader");

    function handleScroll() {
        if (window.scrollY > 50) {
            header.classList.add("scrolled");
        } else {
            header.classList.remove("scrolled");
        }
    }

    if (header) {
        handleScroll();
        window.addEventListener("scroll", handleScroll);
    }

    // 2. Mobile Menu Navigation
    const menuToggle = document.getElementById("menuToggle");
    const mobileNavMenu = document.getElementById("mobileNavMenu");
    
    if (menuToggle && mobileNavMenu) {
        menuToggle.addEventListener("click", () => {
            menuToggle.classList.toggle("active");
            mobileNavMenu.classList.toggle("active");
        });
        
        // Close menu when clicking links
        const mobileLinks = document.querySelectorAll(".mobile-link, .mobile-btn");
        mobileLinks.forEach(link => {
            link.addEventListener("click", () => {
                menuToggle.classList.remove("active");
                mobileNavMenu.classList.remove("active");
            });
        });
    }

    // 3. Scroll Reveal Animations (Intersection Observer)
    const revealElements = document.querySelectorAll(".scroll-reveal");
    
    if (revealElements.length > 0) {
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("revealed");
                    // Once animated, no need to track it
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: "0px 0px -50px 0px"
        });

        revealElements.forEach(el => revealObserver.observe(el));
    }

    // 4. Past Projects Filters
    const filterTabs = document.querySelectorAll(".filter-tab");
    const projectCards = document.querySelectorAll(".project-card");

    filterTabs.forEach(tab => {
        tab.addEventListener("click", () => {
            // Remove active classes
            filterTabs.forEach(t => t.classList.remove("active"));
            tab.classList.add("active");

            const filterValue = tab.getAttribute("data-filter");

            projectCards.forEach(card => {
                const category = card.getAttribute("data-category");
                
                // Fade out/in transitions
                if (filterValue === "all" || category === filterValue) {
                    card.style.display = "flex";
                    setTimeout(() => {
                        card.style.opacity = "1";
                        card.style.transform = "translateY(0)";
                    }, 50);
                } else {
                    card.style.opacity = "0";
                    card.style.transform = "translateY(15px)";
                    setTimeout(() => {
                        card.style.display = "none";
                    }, 300);
                }
            });
        });
    });

    // Helper function to format numbers with Indian numbering system (e.g. 1,35,000)
    const formatCounterNumber = (num, padZero = false) => {
        if (padZero && num < 10) {
            return "0" + num;
        }
        return num.toLocaleString("en-IN");
    };

    // Smooth RAF counter runner with ease-out cubic
    const runCounterAnimation = (el, target, duration = 1800, padZero = false) => {
        const startTime = performance.now();

        const update = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const easeProgress = 1 - Math.pow(1 - progress, 3);
            const currentVal = Math.floor(easeProgress * target);

            el.textContent = formatCounterNumber(currentVal, padZero);

            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                el.textContent = formatCounterNumber(target, padZero);
            }
        };

        requestAnimationFrame(update);
    };

    // 5A. Hero Impact Stats Counter Animation Trigger
    const heroStatsStrip = document.getElementById("heroStatsStrip");
    const heroCounters = document.querySelectorAll(".hero-counter");
    let heroCountersStarted = false;

    const startHeroCounters = () => {
        if (heroCountersStarted) return;
        heroCountersStarted = true;
        heroCounters.forEach(counter => {
            const target = parseInt(counter.getAttribute("data-val"), 10);
            const pad = counter.getAttribute("data-pad") === "true";
            runCounterAnimation(counter, target, 2000, pad);
        });
    };

    if (heroStatsStrip && heroCounters.length > 0) {
        const heroObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    startHeroCounters();
                    heroObserver.disconnect();
                }
            });
        }, { threshold: 0.15 });

        heroObserver.observe(heroStatsStrip);
    }

    // 5B. Research Publications Stats Counter Animation Trigger
    const statsSection = document.getElementById("research");
    const statNums = document.querySelectorAll(".stat-num");
    let researchCountersStarted = false;

    const startResearchCounters = () => {
        if (researchCountersStarted) return;
        researchCountersStarted = true;
        statNums.forEach(num => {
            const target = parseInt(num.getAttribute("data-val"), 10);
            runCounterAnimation(num, target, 2000, false);
        });
    };

    if (statsSection && statNums.length > 0) {
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    startResearchCounters();
                    statsObserver.disconnect();
                }
            });
        }, { threshold: 0.15 });

        statsObserver.observe(statsSection);
    }
});

// 6. Case Study Detail Slide-Over Drawer Functions
function openProjectDrawer(projectId) {
    const data = projectDatabase[projectId];
    if (!data) return;

    // Fill content
    document.getElementById("drawerLogo").src = data.logo;
    document.getElementById("drawerLogo").alt = data.title + " Logo";
    document.getElementById("drawerTag").innerText = data.tag;
    document.getElementById("drawerTitle").innerText = data.title;
    document.getElementById("drawerAbout").innerText = data.about;

    // Generate Approach List Items
    const approachContainer = document.getElementById("drawerApproach");
    approachContainer.innerHTML = "";
    data.approach.forEach(item => {
        const li = document.createElement("li");
        li.innerText = item;
        approachContainer.appendChild(li);
    });

    // Generate Impact Metric Badges
    const impactContainer = document.getElementById("drawerImpact");
    impactContainer.innerHTML = "";
    data.impact.forEach(metric => {
        const div = document.createElement("div");
        div.className = "impact-item";
        
        const valSpan = document.createElement("span");
        valSpan.className = "impact-val";
        valSpan.innerText = metric.val;
        
        const descSpan = document.createElement("span");
        descSpan.className = "impact-desc";
        descSpan.innerText = metric.desc;
        
        div.appendChild(valSpan);
        div.appendChild(descSpan);
        impactContainer.appendChild(div);
    });

    // Open overlay drawer
    const drawer = document.getElementById("projectDrawer");
    drawer.classList.add("active");
    
    // Prevent main body scroll
    document.body.style.overflow = "hidden";

    // Bind Esc key listener
    document.addEventListener("keydown", escCloseListener);
}

function closeProjectDrawer(event) {
    // If event is passed, check if close target is valid
    if (event && event.target !== document.getElementById("projectDrawer") && !event.target.classList.contains("drawer-close")) {
        return;
    }
    
    const drawer = document.getElementById("projectDrawer");
    drawer.classList.remove("active");
    
    // Restore main body scroll
    document.body.style.overflow = "";

    // Unbind Esc key listener
    document.removeEventListener("keydown", escCloseListener);
}

function escCloseListener(e) {
    if (e.key === "Escape") {
        closeProjectDrawer();
    }
}

// 7. Contact Form Handling
function handleFormSubmit(event) {
    event.preventDefault();

    const clientName = document.getElementById("clientName").value;
    const email = document.getElementById("clientEmail").value;
    const message = document.getElementById("clientMsg").value;

    if (!clientName || !email || !message) {
        alert("Please fill in all required fields.");
        return;
    }

    // Toggle forms and show success state
    document.getElementById("contactForm").style.display = "none";
    document.getElementById("formSuccessMessage").style.display = "block";
}

function resetContactForm() {
    // Reset form elements
    document.getElementById("contactForm").reset();
    
    // Toggle containers back
    document.getElementById("formSuccessMessage").style.display = "none";
    document.getElementById("contactForm").style.display = "block";
}
