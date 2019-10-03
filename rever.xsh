$PROJECT = 'pytentiostat'
$ACTIVITIES = ['version_bump',
               'changelog',
               'tag',
               'push_tag',
               'ghrelease',
#               'conda_forge'
               ]

$VERSION_BUMP_PATTERNS = [
    ('pytentiostat/__init__.py', '__version__\s*=.*', "__version__ = '$VERSION'"),
    ('setup.py', 'version\s*=.*,', "version='$VERSION',")
    ]
$CHANGELOG_FILENAME = 'CHANGELOG.rst'
$CHANGELOG_IGNORE = ['TEMPLATE.rst']
$PUSH_TAG_REMOTE ='https://github.com/juami/pytentiostat.git'

$GITHUB_REPO = 'pytentiostat'
$GITHUB_ORG = 'juami'

$LICENSE_URL = 'https://github.com/{}/{}/blob/master/LICENSE'.format($GITHUB_ORG, $GITHUB_REPO)

from urllib.request import urlopen
rns = urlopen('https://raw.githubusercontent.com/juami/mission-control/master/tools/release_not_stub.md').read().decode('utf-8')
$GHRELEASE_PREPEND = rns.format($LICENSE_URL, $PROJECT.lower())
