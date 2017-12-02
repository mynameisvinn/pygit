# pygit
bare bones implementation of git.

### why merkle dags?
it's a merkle tree because commit/tree objects hash hashes. for example, a commit object hashes meta data (date, commit message) as well as the preceding commit's hash. this *directed acyclic graph* of hashes means both structure (bits) and time (sequence of changes) are recorded.

### why commits, trees, blobs?
two commits with the same commit hash id have the same exact content (eg source code) and history (sequence of changes, modifications, git adds).

if they dont, theyll differ in content (ie different tree hashes) or annotation (metadata will be different) or history (different ancestors).

### references
* [a hacker's guide to git](https://wildlyinaccurate.com/a-hackers-guide-to-git/)
* [git from the inside out](https://maryrosecook.com/blog/post/git-from-the-inside-out)