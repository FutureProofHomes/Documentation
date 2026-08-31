(() => {
    const config = [
        {
            title: 'Select Satellite1 Firmware',
            description: 'Which firmware should we flash to your Satellite1?',
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
    ];

    let stage = 0;
    const selections = ['stable']

    function activeStepIndexes() {
        return config.map((_, idx) => idx);
    }

    function isSummaryStage() {
        return !activeStepIndexes().includes(stage);
    }

    function getPreviousStage() {
        const steps = activeStepIndexes();
        if (isSummaryStage()) return steps[steps.length - 1];

        const idx = steps.indexOf(stage);
        return idx > 0 ? steps[idx - 1] : stage;
    }

    function getNextStage() {
        const steps = activeStepIndexes();
        const idx = steps.indexOf(stage);
        return idx >= 0 && idx < steps.length - 1 ? steps[idx + 1] : config.length;
    }

    function selectedLabel(idx) {
        return config[idx].title.replace(/^Select\b/, 'Selected');
    }

    function selectedValue(selected, idx) {
        if (idx !== 0) return selected.title;

        const version = firmwareVersion(selected);
        return `${selected.title}${version ? ` (${version})` : ''}`;
    }

    function choiceTitle(choice, idx) {
        if (idx !== 0) return choice.title;

        const version = firmwareVersion(choice);
        return `${choice.title}${version ? ` (${version})` : ''}`;
    }

    function firmwareVersion(choice) {
        return window.fphFirmwareVersions?.[choice.id] || '';
    }

    function firmwareReleaseUrl(choice) {
        const version = firmwareVersion(choice);
        return window.fphFirmwareReleaseUrls?.[choice.id]
            || (version ? `https://github.com/FutureProofHomes/Satellite1-ESPHome/releases/tag/${version}/` : '');
    }

    function releaseLink(choice, className = 'firmware-release-link') {
        const releaseUrl = firmwareReleaseUrl(choice);
        if (!releaseUrl) return null;

        return el('a', {
            className,
            href: releaseUrl,
            textContent: 'Read release notes',
            attr: {
                target: '_blank',
                rel: 'noopener',
            },
        });
    }

    function summaryRow(label, value) {
        const row = el('p');
        row.append(
            el('strong', { textContent: label }),
            document.createTextNode(`: ${value}`)
        );
        return row;
    }

    function firmwareSummaryRow(selected) {
        const version = firmwareVersion(selected);
        const releaseUrl = firmwareReleaseUrl(selected);
        const row = el('p');
        row.append(
            el('strong', { textContent: selectedLabel(0) }),
            document.createTextNode(': ')
        );

        if (releaseUrl) {
            row.append(el('a', {
                href: releaseUrl,
                textContent: selectedValue(selected, 0),
                attr: {
                    target: '_blank',
                    rel: 'noopener',
                    'aria-label': `Read release notes for ${selected.title} ${version}`,
                },
            }));
        } else {
            row.append(document.createTextNode(selectedValue(selected, 0)));
        }

        return row;
    }

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
        const steps = activeStepIndexes();
        const currentPosition = steps.indexOf(stage);
        const completedPosition = isSummaryStage() ? steps.length : currentPosition;
        steps.forEach((_, idx) => {
            const dot = el('div', {
                className: 'dot',
                attr: { 'aria-current': idx === currentPosition ? 'step' : 'false' }
            })
            if (idx === currentPosition) dot.classList.add('active');
            else if (idx < completedPosition) dot.classList.add('done');
            fragment.appendChild(dot);
        });
        nav.appendChild(fragment);
        return nav;
    }

    function getBackBtn() {
        const hasPrevious = isSummaryStage() || activeStepIndexes().indexOf(stage) > 0;
        const back = el('button', {
            className: 'md-button md-button--secondary',
            textContent: '← Back',
            disabled: !hasPrevious,
            onclick: (e) => {
                e.stopPropagation();
                stage = getPreviousStage();
                render();
            }
        });

        if (!hasPrevious) {
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
                        stage = getNextStage();
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
            const isFirmwareStep = stage === 0;
            const btn = el(isFirmwareStep ? 'div' : 'button', {
                className: 'choice-btn',
                dataset: { id: choice.id },
                tabIndex: 0,
                attr: {
                    role: 'radio',
                    'aria-checked': checked
                },
                onclick: render,
                onkeydown: (e) => {
                    if (!isFirmwareStep || !['Enter', ' '].includes(e.key)) return;
                    e.preventDefault();
                    btn.click();
                }
            })

            btn.append(
                el('span', {
                    className: 'choice-check',
                    textContent: '✓',
                    attr: { 'aria-hidden': 'true' },
                }),
                el('span', {
                    className: 'choice-label',
                    textContent: choiceTitle(choice, stage),
                })
            );

            if (checked) btn.classList.add('selected');

            const link = isFirmwareStep ? releaseLink(choice) : null;
            if (link) {
                const choiceWrapper = el('div', { className: 'choice-option' });
                choiceWrapper.append(btn, link);
                fragment.appendChild(choiceWrapper);
            } else {
                fragment.appendChild(btn);
            }
        });

        choicesDiv.appendChild(fragment);
        section.append(choicesDiv);
        section.append(navigation());
        return section;
    }

    function summary() {
        const section = el('section', { className: 'md-typeset' });
        const fragment = document.createDocumentFragment();
        activeStepIndexes().forEach((idx) => {
            const step = config[idx];
            const selected = step.choices.find(i => i.id === selections[idx]);
            if (!selected) return;
            fragment.appendChild(
                idx === 0 ? firmwareSummaryRow(selected) : summaryRow(selectedLabel(idx), selectedValue(selected, idx))
            );
        });
        fragment.appendChild(
            summaryRow(
                'Selected mmWave',
                'Automatically supports both LD2410 and LD2450 if/when a sensor is attached.'
            )
        );
        const firmware = selections[0] === 'stable' ? '' : `-${selections[0]}`;
        section.append(
            el('h2', { textContent: 'Summary' }),
            fragment,
            navigation(
                `https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest${firmware}.json`
            )
        );
        return section;
    }

    function handleChoice(e) {
        const btn = e.target.closest('.choice-btn');
        if (!btn) return;
        const group = btn.closest('.choices');
        if (group && group.dataset.step) {
            const step = Number(group.dataset.step);
            selections[step] = btn.dataset.id;
            render();
        }
    }

    function render() {
        const el = document.getElementById('firmware-selector');
        if (el) {
            const renderStep = !isSummaryStage();
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