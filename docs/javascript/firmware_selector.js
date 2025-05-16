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
    const selections = ['stable', 'default']

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

    function getBackBtn() {
        const back = el('button', {
            className: 'md-button md-button--secondary',
            textContent: 'Back',
            disabled: stage <= 0,
            onclick: (e) => {
                e.stopPropagation();
                stage -= 1;
                render();
            }
        });

        if (stage <= 0) {
            back.classList.add('hidden');
        }
        return back
    }

    function navigation(manifestUrl) {
        const nav = el('div', { className: 'flex-container' })
        if (manifestUrl) {
            const installBtnWrapper = el('esp-web-install-button', {
                attr: {
                    manifest: manifestUrl,
                    'install-supported': true
                }
            });

            const unsupported = el('div', {
                className: 'admonition failure',
                attr: {
                    slot: 'unsupported'
                }
            });

            unsupported.append(
                el('p', {
                    textContent: 'Failure',
                    className: 'admonition-title',
                }),
                el('p', {
                    textContent: 'Your browser does not support installing things on ESP devices. Use Google Chrome or Microsoft Edge.',
                })
            );

            const notAllowed = el('div', {
                className: 'admonition failure',
                attr: {
                    slot: 'not-allowed'
                }
            });

            notAllowed.append(
                el('p', {
                    textContent: 'Failure',
                    className: 'admonition-title',
                }),
                el('p', {
                    textContent: 'Ah snap, you are not allowed to use this on HTTP!',
                })
            );

            const installContainer = el('div', {
                className: 'flex-container',
                attr: {
                    slot: 'activate'
                }
            });

            const installBtn = el('button', {
                id: 'install-button',
                textContent: 'Install',
                className: 'md-button md-button--primary',
            });

            installContainer.append(
                getBackBtn(),
                dots(),
                installBtn
            );

            installBtnWrapper.append(
                installContainer,
                unsupported,
                notAllowed,
            );
            nav.append(installBtnWrapper);
        } else {
            nav.append(
                getBackBtn(),
                dots(),
                el('button', {
                    className: 'md-button md-button--primary',
                    textContent: 'Next',
                    onclick: (e) => {
                        e.stopPropagation();
                        stage += 1;
                        render();
                    }
                })
            );
        }
        return nav
    }

    function step() {
        const section = el('section', {
            className: 'md-typeset',
            attr: {
                role: 'group',
                'aria-labelledby': 'step-title'
            }
        })

        section.append(el('h2', {
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
                onclick: render
            })

            if (checked) btn.classList.add('selected');
            fragment.appendChild(btn);
        });

        choicesDiv.appendChild(fragment);
        section.append(choicesDiv);
        section.append(navigation());
        return section;
    }

    function summary() {
        const section = el('section', { className: 'md-typeset' });
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
            el('h2', { textContent: 'Summary' }),
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
            el.append(renderStep ? step() : summary());
            
            const next = Array.from(document.getElementsByClassName('next-steps'));
            next.forEach(step => {
                if (renderStep) {
                  step.classList.remove('visible');
                } else {
                  step.classList.add('visible');
                }
            })
        }
    }

    document.addEventListener('DOMContentLoaded', () => {
        window.document$.subscribe(render);
    });
})()