const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const { test } = require('node:test');
const html = readFileSync(join(__dirname, '../term-loan-calculator.html'), 'utf8');
// Run the production calculation functions without the presentation layer.
function source(name) {
  const start = html.indexOf(`  function ${name}(`);
  assert.ok(start >= 0, `Missing production function ${name}`);
  const end = html.indexOf('\n  function ', start + 1);
  return html.slice(start, end);
}
const context = vm.createContext({ setFieldValue() {} });
for (const name of ['parseValue','paymentFromLoan','amountFromPayment','termFromPayment','annualRateFromPayment','solveScenario']) {
  vm.runInContext(source(name), context);
}
const scenario = overrides => ({amount:350000,rateAnnual:10.5,monthlyRate:10.5/1200,termYears:10,months:120,payment:4722.72,cashAvailable:0,solveField:'payment',...overrides});
test('standard amortized monthly payment', () => assert.ok(Math.abs(context.solveScenario(scenario()).payment - 4722.72) < 0.005));
test('explicit zero interest gives principal-only repayment', () => {
  const result = context.solveScenario(scenario({rateAnnual:0,monthlyRate:0}));
  assert.ok(Math.abs(result.payment - 350000/120) < 0.0001);
  assert.ok(Math.abs(result.totalInterest) < 0.0001);
});
test('blank and malformed rates cannot silently become zero', () => {
  for (const value of ['', ' ', 'abc', '1.2.3']) {
    assert.ok(Number.isNaN(context.parseValue(value)));
    assert.throws(() => context.solveScenario(scenario({rateAnnual:context.parseValue(value)})), /valid number/);
  }
  assert.equal(context.parseValue('0'),0);
  assert.equal(context.parseValue('$350,000.00'),350000);
});
test('negative interest is rejected', () => assert.throws(() => context.solveScenario(scenario({rateAnnual:-1,monthlyRate:-1/1200})), /required/));
test('unbounded schedules and nonfinite inputs are rejected', () => {
  assert.throws(() => context.solveScenario(scenario({months:1201})), /100 years/);
  assert.throws(() => context.solveScenario(scenario({amount:Infinity})), /valid number/);
});
test('optional cash input must be a valid nonnegative amount', () => {
  for (const cashAvailable of [-1,NaN,Infinity]) assert.throws(() => context.solveScenario(scenario({cashAvailable})), /cash available/);
});
test('reverse solvers recover the same loan', () => {
  const payment=context.paymentFromLoan(350000,10.5/1200,120);
  assert.ok(Math.abs(context.amountFromPayment(payment,10.5/1200,120)-350000)<0.01);
  assert.ok(Math.abs(context.termFromPayment(350000,10.5/1200,payment)-120)<0.001);
  assert.ok(Math.abs(context.annualRateFromPayment(350000,120,payment)-10.5)<0.001);
});
test('payment below accrued interest cannot amortize', () => assert.throws(()=>context.termFromPayment(350000,10.5/1200,100), /too low/));
