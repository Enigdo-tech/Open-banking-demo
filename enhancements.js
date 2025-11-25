// FinConnect Canada - Enhancement Script
// Add this to demo.html to complete all missing features

// ===== 1. PERSONA SWITCHER =====
function addPersonaSwitcher() {
    const header = document.querySelector('.main-content');
    if (!header) return;

    const switcher = document.createElement('div');
    switcher.style.cssText = 'position: fixed; top: 1rem; left: 270px; z-index: 999; background: rgba(30, 41, 59, 0.95); padding: 0.5rem 1rem; border-radius: 8px; border: 1px solid rgba(148, 163, 184, 0.1);';
    switcher.innerHTML = `
        <select id="personaSwitcher" style="background: rgba(0,0,0,0.3); border: 1px solid rgba(148,163,184,0.3); border-radius: 8px; color: white; padding: 0.5rem 1rem; cursor: pointer;">
            <option value="stabilizer">👔 Stabilizer</option>
            <option value="hustler">🚗 Hustler</option>
            <option value="builder">💼 Builder</option>
        </select>
    `;
    document.body.appendChild(switcher);

    document.getElementById('personaSwitcher').value = currentPersona;
    document.getElementById('personaSwitcher').addEventListener('change', async (e) => {
        currentPersona = e.target.value;
        await loadDashboardData();
    });
}

// ===== 2. PAYMENT SAFETY CHECK MODAL =====
function createModal() {
    const modalHTML = `
        <div id="paymentModal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.8); z-index: 9999; align-items: center; justify-content: center;">
            <div class="modal-content" style="background: #1e293b; border-radius: 16px; padding: 2rem; max-width: 500px; border: 1px solid rgba(148,163,184,0.1);">
                <h3 style="margin-bottom: 1rem; color: #f59e0b;">⚠️ Insufficient Funds Warning</h3>
                <p id="modalMessage" style="color: #94a3b8; margin-bottom: 2rem;"></p>
                <div style="display: flex; gap: 1rem;">
                    <button onclick="closeModal()" class="btn btn-outline" style="flex: 1;">Cancel</button>
                    <button id="modalConfirm" class="btn" style="flex: 1;">Pay from Alternative Account</button>
                </div>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHTML);
}

function showPaymentWarning(billName, billAmount, fromAccount, toAccount) {
    const modal = document.getElementById('paymentModal');
    const message = document.getElementById('modalMessage');
    message.textContent = `Warning: Insufficient funds in ${fromAccount.label} ($${fromAccount.balance}). Would you like to pay ${billName} ($${billAmount}) from ${toAccount.label} ($${toAccount.balance}) instead?`;
    modal.style.display = 'flex';

    document.getElementById('modalConfirm').onclick = () => {
        alert(`Payment of $${billAmount} processed from ${toAccount.label}`);
        closeModal();
    };
}

function closeModal() {
    document.getElementById('paymentModal').style.display = 'none';
}

// ===== 3. INFLATION ALERT (PFM) =====
function addInflationAlerts() {
    // Add to bill data
    const billsWithInflation = [
        { name: "Toronto Hydro", current: 127.50, lastYear: 110.00 },
        { name: "Groceries (Avg)", current: 450.00, lastYear: 380.00 }
    ];

    let alertHTML = '<div class="insight-card" style="background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3);"><div class="insight-icon">📈</div><h3>Inflation Alert</h3>';

    billsWithInflation.forEach(bill => {
        const increase = ((bill.current - bill.lastYear) / bill.lastYear * 100).toFixed(1);
        if (increase > 10) {
            alertHTML += `<p style="color: #94a3b8; margin: 0.5rem 0;"><strong>${bill.name}:</strong> $${bill.current} <span class="badge badge-warning">↑ ${increase}% YoY</span></p>`;
        }
    });

    alertHTML += '</div>';
    return alertHTML;
}

// ===== 4. PROGRESS BAR (PAYROLL) =====
function createAccruedWagesProgress() {
    const accrued = 847.50;
    const total = 1300.00;
    const percentage = (accrued / total * 100).toFixed(0);
    const daysLeft = 5;

    return `
        <div class="glass-panel">
            <h3>Earned Wage Access</h3>
            <div style="background: rgba(255, 255, 255, 0.05); padding: 1.5rem; border-radius: 8px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
                    <div>
                        <div style="color: #94a3b8; font-size: 0.875rem;">Accrued this period</div>
                        <div style="font-size: 2rem; font-weight: bold;">$${accrued}</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="color: #94a3b8; font-size: 0.875rem;">Total pay period</div>
                        <div style="font-size: 1.5rem; font-weight: bold; color: #94a3b8;">$${total}</div>
                    </div>
                </div>
                <div class="progress-bar" style="height: 12px; margin: 1rem 0;">
                    <div class="progress-fill" style="width: ${percentage}%;"></div>
                </div>
                <div style="display: flex; justify-content: space-between; color: #94a3b8; font-size: 0.875rem; margin-bottom: 1rem;">
                    <span>${percentage}% of pay period complete</span>
                    <span>${daysLeft} days until payday</span>
                </div>
                <button class="btn" style="width: 100%;">Access $500 Now (No Interest)</button>
            </div>
        </div>
    `;
}

// ===== 5. PIE CHART (WEALTH) =====
function createPieChart(cash, investments) {
    const total = cash + investments;
    const cashPercent = (cash / total * 100).toFixed(1);
    const investPercent = (investments / total * 100).toFixed(1);

    return `
        <div class="glass-panel" style="text-align: center;">
            <h3 style="margin-bottom: 2rem;">Net Worth Breakdown</h3>
            <div style="position: relative; width: 200px; height: 200px; margin: 0 auto 2rem; border-radius: 50%; background: conic-gradient(#10b981 0% ${cashPercent}%, #6366f1 ${cashPercent}% 100%);">
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background: #1e293b; width: 140px; height: 140px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-direction: column;">
                    <div style="font-size: 2rem; font-weight: bold;">$${(total / 1000).toFixed(0)}k</div>
                    <div style="font-size: 0.875rem; color: #94a3b8;">Total</div>
                </div>
            </div>
            <div style="display: flex; justify-content: center; gap: 2rem;">
                <div>
                    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                        <div style="width: 12px; height: 12px; background: #10b981; border-radius: 50%;"></div>
                        <span style="color: #94a3b8; font-size: 0.875rem;">Cash</span>
                    </div>
                    <div style="font-weight: bold;">${cashPercent}%</div>
                </div>
                <div>
                    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                        <div style="width: 12px; height: 12px; background: #6366f1; border-radius: 50%;"></div>
                        <span style="color: #94a3b8; font-size: 0.875rem;">Investments</span>
                    </div>
                    <div style="font-weight: bold;">${investPercent}%</div>
                </div>
            </div>
        </div>
    `;
}

// ===== 6. FEE COMPARISON WIDGET (WEALTH) =====
function createFeeComparison() {
    const highFeeAmount = 45000;
    const highFeeMER = 2.3;
    const lowFeeMER = 0.08;
    const years = 30;
    const annualReturn = 7;

    // Calculate 30-year impact
    const highFeeCost = highFeeAmount * (Math.pow(1 + (annualReturn - highFeeMER) / 100, years) - Math.pow(1 + annualReturn / 100, years));
    const lowFeeCost = highFeeAmount * (Math.pow(1 + (annualReturn - lowFeeMER) / 100, years) - Math.pow(1 + annualReturn / 100, years));
    const savings = Math.abs(highFeeCost - lowFeeCost);

    return `
        <div class="glass-panel">
            <h3 style="margin-bottom: 1.5rem;">Fee Analyzer</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.5rem;">
                <div style="background: rgba(239, 68, 68, 0.1); padding: 1rem; border-radius: 8px; border: 1px solid rgba(239, 68, 68, 0.3);">
                    <div style="color: #94a3b8; font-size: 0.875rem; margin-bottom: 0.5rem;">High-Fee Mutual Fund</div>
                    <div style="font-weight: bold; margin-bottom: 0.5rem;">Institution A</div>
                    <div style="font-size: 1.5rem; font-weight: bold; color: #ef4444;">MER: ${highFeeMER}%</div>
                    <div style="color: #94a3b8; font-size: 0.875rem; margin-top: 0.5rem;">$${highFeeAmount.toLocaleString()} invested</div>
                </div>
                <div style="background: rgba(16, 185, 129, 0.1); padding: 1rem; border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.3);">
                    <div style="color: #94a3b8; font-size: 0.875rem; margin-bottom: 0.5rem;">Low-Fee ETF</div>
                    <div style="font-weight: bold; margin-bottom: 0.5rem;">Institution C</div>
                    <div style="font-size: 1.5rem; font-weight: bold; color: #10b981;">MER: ${lowFeeMER}%</div>
                    <div style="color: #94a3b8; font-size: 0.875rem; margin-top: 0.5rem;">Recommended alternative</div>
                </div>
            </div>
            <div class="insight-card" style="background: rgba(16, 185, 129, 0.1); border-color: rgba(16, 185, 129, 0.3);">
                <div class="insight-icon">💰</div>
                <h3>30-Year Impact</h3>
                <p style="color: #94a3b8; margin-bottom: 1rem;">By switching to a low-fee ETF, you could save approximately <strong style="color: #10b981;">$${Math.round(savings / 1000)}k</strong> over ${years} years.</p>
                <button class="btn">Switch to Low-Fee ETF</button>
            </div>
        </div>
    `;
}

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', () => {
    // Wait for dashboard to load
    setTimeout(() => {
        if (document.getElementById('dashboardLayout') && !document.getElementById('dashboardLayout').classList.contains('hidden')) {
            addPersonaSwitcher();
            createModal();
        }
    }, 1000);
});

// Export functions for use in main demo
window.FinConnectEnhancements = {
    addPersonaSwitcher,
    showPaymentWarning,
    addInflationAlerts,
    createAccruedWagesProgress,
    createPieChart,
    createFeeComparison
};
