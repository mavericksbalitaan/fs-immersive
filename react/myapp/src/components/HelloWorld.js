import '../stylesheets/index.css'
import styles from '../stylesheets/Title.module.css'

export default function HelloWorld() {
  return (
    <>
      <p className={styles.title}>Welcome</p>
      <p id="hello">Hello</p>
    </>
  )
}



