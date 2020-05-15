import pytz
import pytest
from datetime import datetime
from mock import Mock, MagicMock, patch

from updatechangelog import common


def test_nothing_new():
    os_mock = Mock()
    os_mock.getcwd.return_value = ''
    mock_Repo = MagicMock()
    with patch.multiple(common, os=os_mock, Repo=mock_Repo):
        with pytest.raises(SystemExit, match=r'0'):
            common.main()


def test_rendering():
    template = common.get_template()
    messages = ["First entry", "Second entry"]
    name = 'Fake Name'
    email = 'fake@example.com'
    added = [
        'first_added.patch',
        'second_added.patch'
    ]
    modified = [
        'first_modified.patch',
        'second_modified.patch'
    ]
    deleted = [
        'first_deleted.patch',
        'second_deleted.patch'
    ]
    current_dt = datetime.now().replace(tzinfo=pytz.utc)

    changelog_entry = template.render(
        messages=messages,
        added=added,
        modified=modified,
        deleted=deleted,
    ).strip()
    expected = ''
    with open('tests/expected.output', 'r') as f:
        expected = f.read().strip()
    assert changelog_entry == expected


@pytest.mark.skip
def test_new_commit():
    os_mock = Mock()
    os_mock.getcwd.return_value = ''
    mock_Repo = MagicMock()

    mock_commit1 = MagicMock()
    mock_commit1.configure_mock(
        hexsha = 'abcdef12345'
    )
    mock_commit1.tree.side_effect = [
        {'salt': [Mock(path='existing.patch')]},
    ]

    mock_commit2 = MagicMock()
    mock_commit2.configure_mock(
        hexsha = 'abcdef12345'
    )
    mock_commit2.tree.side_effect = [
        {'salt': [Mock(path='current.patch')]},
    ]

    mock_Repo.return_value.commit.side_effects = [
        mock_commit1,
        mock_commit2
    ]
    with patch.multiple(common, os=os_mock, Repo=mock_Repo):
        with pytest.raises(SystemExit, match=r'0'):
            common.main()
