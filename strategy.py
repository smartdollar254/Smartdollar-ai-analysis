class ConfluenceTrading:
    def __init__(self):
        self.confidence_scores = {'BUY': 0, 'SELL': 0, 'NO_TRADE': 0}

    def analyze_signals(self, signals):
        # Assuming signals is a list of tuples with (signal_type, confidence)
        for signal_type, confidence in signals:
            if signal_type in self.confidence_scores:
                self.confidence_scores[signal_type] += confidence

    def decision(self):
        max_signal = max(self.confidence_scores, key=self.confidence_scores.get)
        confidence_score = self.confidence_scores[max_signal] / sum(self.confidence_scores.values())
        if confidence_score > 0.5:
            return max_signal, confidence_score
        else:
            return 'NO_TRADE', 0

# Example usage:
# signals = [('BUY', 0.6), ('SELL', 0.3), ('BUY', 0.2)]
# engine = ConfluenceTrading()
# engine.analyze_signals(signals)
# decision, confidence = engine.decision()  # Should return ('BUY', confidence_score) if confidence exceeds 50%