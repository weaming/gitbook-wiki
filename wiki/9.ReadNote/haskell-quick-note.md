### Keywords

--- 表示省略

- where
- let --- in
- case --- of (->)
- .. (列表生成式)
- ::
- data --- [deriving (---)]
- type
- $ (Function application, 隔绝函数参数，达到少写括号效果，优先级最低)
- . (组合函数，右向关联)
- class --- where --- (Rust的trait)
- instance --- where --- (Rust的impl)
- infixl
- infixr

### Position switch

- () 中置运算符前置
- \`\` 前置运算符中置

### Concepts

- Pattern matching (=)
- Currying
- Guard (|)
- Lambda
- Recursion
- Typeclass
- Constructor
    - value constructor
    - type constructor
        - Maybe
    - Kind
- Functor `<$>` fmap
- Applicative `<*>` liftA
- Monad `>>=` liftM

### Types

- Num
- Float
- Int
- Integer
- Char
- String

### Typeclasses

- Ord
- Eq
- Show
- Read
- Functor
- Applicative
- Monad

### Monoid
The `Monoid` type class is defined in `import Data.Monoid`

functions:
- mempty
- mappend
- mconcat

### Type system

Types are little labels that values carry so that we can reason about the values.
But types have their own little labels, called kinds.
A kind is more or less the type of a type.

### Data Structure

- List
- Tuple
- Map
- Set
- ... (data/type/newtype)
- ByteString

### GHCI commands

- :l    load modules from file
- :r    reload modules
- :t    display type of some value
- :info show information of a typeclass
- :k    display kind of some type

### 运算符优先级

在 `ghci` 通过 `:info ?` 来获得，`?` 代表具体运算符。数字越大，优先级越高。优先级范围为 0 到 9。
默认函数和参数结合的优先级最高，可以想象为10。

例子：`2 ^ (+3) 2`, `(+1) . (^2) $ 3` 可行，而 `(+1) . (^2) 3` 不可行(函数`(^2)`和参数`3`优先结合，函数`(+1)`无法与值`9`形成组合函数)

- 0.`$` `->`
- 1.`>>=`
- 4.`<*>` `<$>` `<` `>` `>=` `<=` `==` `/=`
- 5.`++` `:`
- 6.`+` `-`
- 7.`*` `/`
- 8.`^`
- 9.`.`

`<$>`:
```
(<$>) :: (Functor f) => (a -> b) -> f a -> f b
f <$> x = fmap f x
```

### Functor

Type constructor

If we want to make a type constructor an instance of Functor, it has to have a kind of `* -> *`,
which means that it has to take exactly one concrete type as a type parameter.

`f` plays the role of our functor instance here:
```
class Functor f where
    fmap :: (a -> b) -> f a -> f b
```

`Maybe` is one of type constructor, `Nothing` and `Just a` are all the result values produced by `Maybe`.
Value `maybe 3` has the type `Maybe Int`(?)

`f` is a function has type `(a -> b)`:
```
data Maybe a = Nothing | Just a
instance Funcotr Maybe where
    fmap f (Just a) = Just (f x)
    fmap f Nothing = Nothing

instance Functor IO where
    fmap f action = do
        result <- action
        return (f result)

instance Functor (Either a) where
    fmap f b = Either a (f b)

# We usually mark functions that take anything and return anything as a -> b
instance Functor ((->) r) where
    fmap f g = (\x -> f (g x))
```

#### Two laws of functors

1. **if we map the id function over a functor, the functor that we get back should be the same as the original functor.**
2. **composing two functions and then mapping the resulting function over a functor should be the same as first mapping one function over the functor and then mapping the other one.**

```
fmap id = id
fmap (f . g) = fmap f . fmap g
fmap (f . g) F = fmap f (fmap g F)
```

### Applicative

`f` plays the role of our applicative functor instance here:
```
class Functor f => Applicative f where
    pure :: a -> f a
    <*> :: f (a -> b) -> f a -> f b

instance Applicative Maybe where
    pure = Just
    Nothing <*> _ = Nothing
    (Just f) <*> something = fmap f something

instance Applicative [] where
    pure x = [x]
        fs <*> xs = [f x | f <- fs, x <- xs] >>]*>

instance Applicative IO where
    pure = return
    a <*> b = do
        f <- a
        x <- b
        return (f x)

instance applicative ((->) r) where
    pure x = (\_ -> x)
    f <*> g = \x -> f x (g x)
```

```
liftA2 :: (Applicative f) => (a -> b -> c) -> f a -> f b -> f c
liftA2 f a b = f <$> a <*> b

sequenceA :: (Applicative f) => [f a] -> f [a]
sequenceA [] = pure []
sequenceA (x:xs) = (:) <$> x <*> sequenceA xs

sequenceA :: (Applicative f) => [f a] -> f [a]
sequenceA = foldr (liftA2 (:)) (pure [])
```

`pure` should take a value of any type and return an applicative functor with that value inside it.

```
ghci> pure "Hey" :: [String]
["Hey"]
ghci> pure "Hey" :: Maybe String
Just "Hey"
```

## Conlusions from articles

1. A `functor` is a data type that implements the `Functor` typeclass.
2. An `applicative` is a data type that implements the `Applicative` typeclass.
3. A `monad` is a data type that implements the `Monad` typeclass.
4. A `Maybe` implements all three, so it is a functor, an applicative, and a monad.

- functors: you apply a function to a wrapped value using `fmap` or `<$>`
- applicatives: you apply a wrapped function to a wrapped value using `<*`> or `liftA`
- monads: you apply a function that returns a wrapped value, to a wrapped value using `>>=` or `liftM`

## Links

- [Learn You a Haskell for Great Good!](http://learnyouahaskell.com/chapters)
- [Functors, Applicatives, And Monads In Pictures](http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html)
