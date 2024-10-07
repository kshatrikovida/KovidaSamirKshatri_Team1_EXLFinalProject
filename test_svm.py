import pytest

@pytest.mark.xfail
@pytest.mark.accuracy
def test_accuracy_svm():
    assert accuracyScores('SVM') >= 75