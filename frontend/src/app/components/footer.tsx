import styles from '../page.module.css';

export default function Footer() {
    return (
        <footer className={styles.footer}>
          <span>© 2025 Lukas P</span>
          <span>
            <a href="https://github.com/Cherlan27/vocable_trainer" target="_blank" rel="noopener noreferrer">GitHub</a>
          </span>
        </footer>
    )
}
