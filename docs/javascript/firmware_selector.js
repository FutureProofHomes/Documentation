(() => {
    const config = [
        {
            title: 'Select Firmware',
            description: 'Choose which firmware you\'ll be using with your device.',
            choices: [
                {
                    id: "stable",
                    title: "Stable",
                },
                {
                    id: "beta",
                    title: "Beta",
                },
            ]
        },
        {
            title: 'Select mmWave Sensor',
            description: 'Which optional mmWave sensor is attached to the Sat1?',
            choices: [
                {
                    id: "default",
                    title: "No sensor",
                },
                {
                    id: "ld2410",
                    title: "LD2410",
                },
                {
                    id: "ld2450",
                    title: "LD2450",
                },
            ]
        },
    ];

    let stage = 0;
    const selections = Array(config.length).fill(null);

    function setAttr(el, obj) {
        Object.entries(obj).forEach(([k, v]) => el[k] = v);
        return el
    }

    function el(tag, {attr = {}, dataset = {}, ...kwargs} = {}) {
        const el = document.createElement(tag);
        Object.entries(attr).forEach(([k, v]) => {
            el.setAttribute(k, v === true ? '' : v);
        });
        setAttr(el, kwargs)
        if (dataset) setAttr(el.dataset, dataset)
        if (tag === 'button') el.type = tag
        return el
    }

    function dots() {
        const nav = el('nav', {
            className: 'progress',
            attr: { 'aria-label': 'Progress' }
        })
        const fragment = document.createDocumentFragment();
        config.forEach((_, idx) => {
            const dot = el('div', {
                className: 'dot',
                attr: { 'aria-current': idx === stage ? 'step' : 'false' }
            })
            if (idx === stage) dot.classList.add('active');
            else if (idx < stage) dot.classList.add('done');
            fragment.appendChild(dot);
        });
        nav.appendChild(fragment);
        return nav;
    }

    function navigation(manifestUrl) {
        const nav = el('div', { className: 'buttons' })
        nav.append(el('button', {
            className: 'md-button md-button--secondary',
            textContent: 'Back',
            disabled: stage === 0,
            onclick: () => { stage--; render(); }
        }));
        if (manifestUrl) {
            nav.append(el('esp-web-install-button', {
                id: 'install-button',
                attr: {
                    manifest: manifestUrl,
                    'install-supported': true
                }
            }));
        }
        return nav
    }

    function step() {
        const section = el('section', {
            attr: {
                role: 'group',
                'aria-labelledby': 'step-title'
            }
        })

        section.append(el('h3', {
            id: 'step-title',
            textContent: config[stage].title,
        }));
        
        if (config[stage].description) {
            section.append(el('p', {
                className: 'step-description',
                textContent: config[stage].description,
            }))
        }

        const choicesDiv = el('div', {
            className: 'choices',
            attr: { role: 'radiogroup' },
            dataset: { step: stage }
        })

        const fragment = document.createDocumentFragment();
        config[stage].choices.forEach((choice, i) => {
            const checked = selections[stage] === choice.id;
            const btn = el('button', {
                className: 'md-button md-button--primary choice-btn',
                textContent: choice.title,
                dataset: { id: choice.id },
                tabIndex: 0,
                attr: {
                    role: 'radio',
                    'aria-checked': checked
                },
                onclick: () => { stage++; render(); }
            })

            if (checked) btn.classList.add('selected');
            fragment.appendChild(btn);
        });

        choicesDiv.appendChild(fragment);
        section.append(choicesDiv);
        if (stage > 0) section.append(navigation());
        return section;
    }

    function summary() {
        const section = el('section');
        const fragment = document.createDocumentFragment();
        config.forEach((step, idx) => {
            const selected = step.choices.find(i => i.id === selections[idx]);
            if (!selected) return;
            fragment.appendChild(
                el('p', { textContent: `${step.title}: ${selected.title}` })
            );
        });
        const firmware = selections[0] === 'stable' ? '' : `-${selections[0]}`;
        const mmwave = selections[1] === 'default' ? '' : `.${selections[1]}`;
        section.append(
            el('h3', { textContent: 'Summary' }),
            fragment,
            navigation(
                `https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest${firmware}${mmwave}.json`
            )
        );
        return section;
    }

    function handleChoice(e) {
        const btn = e.target.closest('.choice-btn');
        if (!btn) return;
        const group = btn.parentElement;
        if (group && group.dataset.step) {
            selections[Number(group.dataset.step)] = btn.dataset.id;
            render();
        }
    }

    function render() {
        const el = document.getElementById('firmware-selector');
        if (el) {
            const renderStep = stage < config.length;
            el.replaceChildren();
            el.addEventListener('click', handleChoice);
            el.append(dots(), renderStep ? step() : summary());
            
            const instructions = document.getElementById('firmware-flash-steps');
            const visible = instructions?.classList.contains('visible');
            if (renderStep && visible) {
                instructions.classList.remove('visible');
            } else if (!renderStep && !visible) {
                instructions.classList.add('visible');
            }
        }
    }

    document.addEventListener('DOMContentLoaded', () => {
        window.document$.subscribe(render);
    });
})()